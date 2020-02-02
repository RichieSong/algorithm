package main

import (
	"fmt"
	"github.com/Shopify/sarama"
	"strings"
	"sync"
	"time"
)

// Config 配置
type Config struct {
	Topic      string `xml:"topic"`
	Broker     string `xml:"broker"`
	Frequency  int    `xml:"frequency"`
	MaxMessage int    `xml:"max_message"`
}

type Producer struct {
	producer  sarama.AsyncProducer
	topic     string
	msgQ      chan *sarama.ProducerMessage
	wg        sync.WaitGroup
	closeChan chan struct{}
}

// NewProducer 构造KafkaProducer
func NewProducer(cfg *Config) (*Producer, error) {

	config := sarama.NewConfig()
	config.Producer.RequiredAcks = sarama.NoResponse                                  // Only wait for the leader to ack
	config.Producer.Compression = sarama.CompressionSnappy                            // Compress messages
	config.Producer.Flush.Frequency = time.Duration(cfg.Frequency) * time.Millisecond // Flush batches every 500ms
	config.Producer.Partitioner = sarama.NewRandomPartitioner

	p, err := sarama.NewAsyncProducer(strings.Split(cfg.Broker, ","), config)
	if err != nil {
		return nil, err
	}
	ret := &Producer{
		producer:  p,
		topic:     cfg.Topic,
		msgQ:      make(chan *sarama.ProducerMessage, cfg.MaxMessage),
		closeChan: make(chan struct{}),
	}

	return ret, nil
}

// Run 运行
func (p *Producer) Run() {

	p.wg.Add(1)
	go func() {
		defer p.wg.Done()

	LOOP:
		for {
			select {
			case m := <-p.msgQ:
				p.producer.Input() <- m
			case err := <-p.producer.Errors():
				if nil != err && nil != err.Msg {
					fmt.Printf("[producer] err=[%s] topic=[%s] key=[%s] val=[%s]", err.Error(), err.Msg.Topic, err.Msg.Key, err.Msg.Value)
				}
			case <-p.closeChan:
				break LOOP
			}

		}
	}()

	for hasTask := true; hasTask; {
		select {
		case m := <-p.msgQ:
			p.producer.Input() <- m
		default:
			hasTask = false
		}
	}

}

// Close 关闭
func (p *Producer) Close() error {
	close(p.closeChan)
	fmt.Printf("[producer] is quiting")
	p.wg.Wait()
	fmt.Printf("[producer] quit over")

	return p.producer.Close()
}

// Log 发送log
func (p *Producer) Log(key string, val string) {
	msg := &sarama.ProducerMessage{
		Topic: p.topic,
		Key:   sarama.StringEncoder(key),
		Value: sarama.StringEncoder(val),
	}

	select {
	case p.msgQ <- msg:
		return
	default:
		fmt.Printf("[producer] err=[msgQ is full] key=[%s] val=[%s]", msg.Key, msg.Value)
	}

}

func main() {
	c := &Config{
		"kafka_test",
		"172.28.60.62:9092,172.28.60.63:9092,172.28.34.98:9092",
		2,
		200,
	}
	p, err := NewProducer(c)
	if err != nil {
		fmt.Println(err)
	}
	p.Run()
	p.Log("go_test", "this a   dsfsdfsfsfsmessage")
	p.Close()
}
