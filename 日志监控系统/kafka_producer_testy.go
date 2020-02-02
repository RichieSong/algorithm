package main

import (
	"fmt"
	"github.com/Shopify/sarama"
	"strconv"
	"strings"
	"time"
)

type Producer_ struct {
	BrokerServers string               `json:"broker_servers"`
	Config        *sarama.Config       `json:"config"`
	SyncProducer  sarama.SyncProducer  `json:"sync_producer"`
	AsyncProducer sarama.AsyncProducer `json:"async_producer"`
}

type Consumer struct {
	BrokerServers string         `json:"broker_servers"`
	Config        *sarama.Config `json:"config"`
}

//获取生产者实例
func (p *Producer) GetSysProducer() error {
	var err error
	p.SyncProducer, err = sarama.NewSyncProducer(strings.Split(p.BrokerServers, ","), p.Config)
	if err != nil {
		fmt.Printf("Create producer failed %s \n", err.Error())
		return err
	}
	fmt.Println("Create producer Success!")
	return nil
}

//批量发送数据到kafka
func (p *Producer) BathProduceMsg(topic, key string, messages []string) error {
	if p.SyncProducer == nil {
		if e := p.GetSysProducer(); e != nil {
			fmt.Printf("Create kafka producer failed: %s \n", e.Error())
		}
	}
	defer p.SyncProducer.Close()
	msgs := make([]*sarama.ProducerMessage, len(messages))
	for i, m := range messages {
		msg := sarama.ProducerMessage{}
		msg.Topic = topic
		msg.Key = sarama.StringEncoder(key)
		msg.Value = sarama.StringEncoder(m)
		msg.Timestamp = time.Now()
		msgs[i] = &msg
	}
	return p.SyncProducer.SendMessages(msgs)
}

//单条发送数据到kafka
func (p *Producer) ProducerMsg(topic, key string, msg string) (partition int32, offset int64, err error) {
	if p.SyncProducer == nil {
		if e := p.GetSysProducer(); e != nil {
			fmt.Printf("Create kafka producer failed: %s \n", e.Error())
		}
	}
	defer p.SyncProducer.Close()
	m := &sarama.ProducerMessage{}
	m.Topic = topic
	m.Key = sarama.StringEncoder(key)
	m.Value = sarama.StringEncoder(msg)
	m.Timestamp = time.Now()
	return p.SyncProducer.SendMessage(m)
}

func main() {

	p := Producer{BrokerServers: "172.28.60.62:9092,172.28.60.63:9092,172.28.34.98:9092"}
	//p.Config.Producer.RequiredAcks = sarama.WaitForAll
	//p.Config.Producer.Partitioner = sarama.NewRandomPartitioner
	//p.Config.Producer.Return.Successes = true
	fmt.Println(strings.Split(p.BrokerServers, ","))
	//p.GetSysProducer()
	var msg []string
	for i := 0; i < 1000; i++ {
		msg = append(msg, "I am song "+strconv.Itoa(i))
	}
	err := p.BathProduceMsg("kafka_test", "nil", msg)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Send to kafka Msg(1000) Success!")
	}

}
