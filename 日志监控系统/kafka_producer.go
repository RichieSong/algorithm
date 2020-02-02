package main

import (
	"fmt"
	"github.com/Shopify/sarama"
	"github.com/astaxie/beego/logs"
	"sync"
	"time"
)

type KafkaProducerInfo struct {
	producer sarama.SyncProducer
	//producer sarama.AsyncProducer
	msg *sarama.ProducerMessage
	Wg  sync.WaitGroup
}

var (
	Kafkaproducerinfo *KafkaProducerInfo
)

// control concurrent equal 10
var tokens = make(chan struct{}, 10)

func InitKafkaProducer() {
	config := sarama.NewConfig()
	config.Producer.RequiredAcks = sarama.WaitForAll          // 三种ack模式 保证数据不丢失
	config.Producer.Partitioner = sarama.NewRandomPartitioner // 生成用于选择要发送消息的分区的分区程序,默认是散列消息密钥
	config.Producer.Return.Successes = true                   // 成功分发的消息将返回到success channel
	//config.Producer.Return.Errors = true                      // 失败分发的消息将返回error channel
	//producer, err := sarama.NewAsyncProducer([]string{"172.28.60.62:9092", "172.28.60.63:9092", "172.28.34.98:9092"}, config)
	//producer, err := sarama.NewAsyncProducer(strings.Split(addrs, ","), config)
	producer, err := sarama.NewSyncProducer([]string{"172.28.60.62:9092"}, config)
	if err != nil {
		logs.Error(" func InitKafkaProducer init instance fail Error: %s", err.Error())
	}

	// send message
	msg := &sarama.ProducerMessage{Topic: "kafka_test", Key: sarama.StringEncoder("go_test")} // go test 什么意思
	//fmt.Println(reflect.TypeOf(producer))
	//fmt.Println(reflect.TypeOf(msg))
	//Kafkaproducerinfo = &KafkaProducerInfo{producer: producer, msg: msg}
	//Kafkaproducerinfo.producer = producer
	//Kafkaproducerinfo.msg = msg
	//KafkaProducer(msg, producer, "this a message")
	v := "this a message"
	for {

		msg.Value = sarama.ByteEncoder(v)

		// send to chain
		//producer.Input() <- msg
		//tokens <- struct{}{} // get tokens
		pid, offset, err := producer.SendMessage(msg)
		//<-tokens // release tokens
		if err != nil {
			fmt.Println("send msg failed, error: ", err)
		}
		fmt.Printf("pid: %d, offset: %d", pid, offset)
	}
}

func main() {
	InitKafkaProducer()
	time.Sleep(time.Second * 10)
}
