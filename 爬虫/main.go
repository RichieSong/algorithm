package main

import (
	"fmt"
	"github.com/PuerkitoBio/goquery"
	"github.com/gocolly/colly"
	_ "github.com/gpmgo/gopm/modules/log"
)

const url = "https://www.zhipin.com/job_detail/?query=go"

type Info struct {
	Position     string
	Salary       string
	Address      string
	Company      string
	Company_type string
	Publish_time string
}

func main() {
	// 框架获取内容
	c := colly.NewCollector()
	c.AllowedDomains = []string{"www.zhipin.com"}
	c.UserAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
	c.OnRequest(func(r *colly.Request) {
		r.Headers.Set("Host", "https://www.zhipin.com")
		r.Headers.Set("Connection", "keep-alive")
		r.Headers.Set("Accept", "*/*")
		r.Headers.Set("Origin", "https://www.zhipin.com")
		r.Headers.Set("Referer", "https://www.zhipin.com/job_detail/?query=go") //关键头 如果没有 则返回 错误
		r.Headers.Set("Accept-Encoding", "gzip, deflate")
		r.Headers.Set("Accept-Language", "zh-CN,zh;q=0.9")
		fmt.Printf("%+v\r\n%+v\r\n", *r, *(r.Headers))
	})
	c.OnHTML(".job-list>ul>li", func(e *colly.HTMLElement) {
		//link := e.Attr("href")
		//fmt.Println(e)
		//c.Visit(e.Request.AbsoluteURL(link)) //获取link 继续获取内容
		e.DOM.Each(func(_ int, s *goquery.Selection) {
			var info Info
			info.Position = s.Find(".info-primary .job-title ").Text()
			info.Salary = s.Find(".info-primary .red ").Text()
			info.Address = s.Find(".info-primary > p ").Text()
			info.Company = s.Find(".info-company .company-text > h3 > a ").Text()
			info.Company_type = s.Find(".info-company .company-text > p ").Text()
			info.Publish_time = s.Find(".info-publis > p ").Text()
			fmt.Printf("Info: %s\n", info)

		})

	})
	//c.OnScraped(func(_ *colly.Response) {
	//	bData, _ := json.MarshalIndent(, "", "\t")
	//	fmt.Println(string(bData))
	//}
	//c.OnError(func(resp *colly.Response, errHttp error) {
	//	//err = errHttp
	//})
	c.Visit(url)
}
