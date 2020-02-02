package main

import (
	"context"
	"fmt"
	"github.com/coreos/etcd/clientv3"
	"sync"
	"time"
)

type EtcdMutex struct {
	ttl     int64              // 租约时间
	conf    clientv3.Config    // etcd集群配置
	key     string             // etcd key
	cannel  context.CancelFunc // 关闭续租的func
	lease   clientv3.Lease
	leaseID clientv3.LeaseID
	txn     clientv3.Txn
}

// 初始化锁
func (em *EtcdMutex) init() error {
	var err error
	var ctx context.Context
	client, err := clientv3.New(em.conf)
	if err != nil {
		return err
	}
	em.txn = clientv3.NewKV(client).Txn(context.TODO())
	em.lease = clientv3.NewLease(client)
	leaseResp, err := em.lease.Grant(context.TODO(), em.ttl)
	em.leaseID = leaseResp.ID
	_, err = em.lease.KeepAlive(ctx, em.leaseID)
	return err
}

// get lock
func (em *EtcdMutex) Lock() error {

	err := em.init()
	if err != nil {
		return err
	}
	// lock
	em.txn.If(clientv3.Compare(clientv3.CreateRevision(em.key), "=", 0)).Then(clientv3.OpPut(em.key, "", clientv3.WithLease(em.leaseID))).Else()
	txnResp, err := em.txn.Commit()
	if err != nil {
		return err
	}
	if !txnResp.Succeeded {
		return fmt.Errorf("抢锁失败")
	}
	return nil
}

// lease lock
func (em *EtcdMutex) Unlock() {
	em.cannel()
	em.lease.Revoke(context.TODO(), em.leaseID)
	fmt.Println("释放了锁")
}

func main() {
	var wg sync.WaitGroup
	var conf = clientv3.Config{
		Endpoints:   []string{"172.28.60.63:2380"},
		DialTimeout: 5 * time.Second,
	}
	eMutex1 := &EtcdMutex{
		conf: conf,
		ttl:  10,
		key:  "lock",
	}
	eMutex2 := &EtcdMutex{
		conf: conf,
		ttl:  10,
		key:  "lock",
	}
	// goroutine
	wg.Add(2)
	go func(wg sync.WaitGroup) {
		err := eMutex1.Lock()
		if err != nil {
			fmt.Println("goroutine1 抢锁失败")
			fmt.Println(err)
			return
		}
		fmt.Println("goroutine1 抢锁成功")
		time.Sleep(10 * time.Second)
		defer func() {
			eMutex1.Unlock()
			wg.Done()
		}()
	}(wg)
	// goroutine2
	go func(wg sync.WaitGroup) {
		err := eMutex2.Lock()
		if err != nil {
			fmt.Println("go 2 get lock failed")
			fmt.Println(err)
			return
		}
		fmt.Println("go 2 get lock success！")
		defer func() {
			eMutex2.Unlock()
			wg.Done()
		}()
	}(wg)
	wg.Wait()
}
