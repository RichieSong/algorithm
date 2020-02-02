package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

var Db *sql.DB

func main() {
	db, err := sql.Open("mysql", "root:songming@tcp(127.0.0.1:3306)/qbops?charset=utf8")
	if err != nil {
		panic(err)
	}
	stmt, err := db.Prepare("select * from schedule_idc where id=?") // xxxx查询并非用prepare
	sele, err := db.Query("select * from schedule_idc")
	//upd, err := db.Prepare("update schedule_idc set a=b where user='songming' ") // 更新
	//upd, err := db.Prepare("insert ") // 插入
	res, err := stmt.Exec(11)      //替换Prepare中的？的值
	ret, err := res.RowsAffected() //返回影响行数
	id, err := res.LastInsertId()
	if err != nil {
		panic(err)
	}
	fmt.Println(id)
	fmt.Println(ret)
	//fmt.Println(sele)
	for sele.Next() {
		var id int
		var name string
		var memo string
		var ips string
		var broadband int
		var abbr string
		var city_id int
		err = sele.Scan(&id, &name, &memo, &ips, &broadband, &abbr, &city_id) // 如果数据库字段为空，而声明的变量类型是string 会报错 nil不是字符串类型
		fmt.Println(err)
		fmt.Println(id, name, broadband, abbr, city_id, ips)
	}

}
