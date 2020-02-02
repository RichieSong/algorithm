package main

import (
	"bufio"
	"fmt"
	"io"
	"net/http"

	"github.com/PuerkitoBio/goquery"
	"golang.org/x/net/html/charset"
	"golang.org/x/text/encoding"
	"golang.org/x/text/transform"
)

const baseUrl = "https://www.zhipin.com/c101010100/h_101010100/?query=python&page=1&ka=page-1"

func main() {

	resp, err := http.Get(baseUrl)
	if err != nil {
		panic("初始化请求错误")
	}
	if resp.StatusCode != http.StatusOK {
		fmt.Printf("请求状态码是 %s \n", resp.StatusCode)
	}

	defer resp.Body.Close()

	htmlEncoding := determineEncoding(resp.Body)
	reader := transform.NewReader(resp.Body, htmlEncoding.NewDecoder())

	// Load the HTML document
	//doc, err := goquery.NewDocumentFromReader(reader)
	//if err != nil {
	//	log.Fatal(err)
	//}

	parseHtml(reader)
	// Find the review items
	//doc.Find(".job-list>ul>li").Each(func(i int, s *goquery.Selection) {
	//	// For each item found, get the band and title
	//	comment := s.Find(".job-primary .detail-bottom .detail-bottom-text").Text()
	//	title := s.Find("a>div.job-title").Text()
	//	URL,_ := s.Find("a").Attr("href")
	//	company := s.Find("div.info-company>div>h3>a").Text()
	//	pay := s.Find("a>span").Text()
	//	address := s.Find("div.info-primary>p").Text()
	//	fmt.Printf("Review %d: %s - %s %s - %s - %s + %s  \n",
	//		i, company, title,URL,pay,address,comment)
	//})
}

func parseHtml(reader io.Reader) {
	// Load the HTML document
	doc, err := goquery.NewDocumentFromReader(reader)
	if err != nil {

	}

	// Find the review items
	doc.Find(".job-list>ul>li").Each(func(i int, s *goquery.Selection) {
		// For each item found, get the band and title
		//comment := s.Find(".job-primary .detail-bottom .detail-bottom-text").Text()
		title := s.Find("a>div.job-title").Text()
		URL, _ := s.Find("a").Attr("href")
		company := s.Find("div.info-company>div>h3>a").Text()
		pay := s.Find("a>span").Text()
		address := s.Find("div.info-primary>p").Text()
		fmt.Printf("Review %d: %s - %s %s - %s - %s + %s  \n",
			i, company, title, URL, pay, address)
	})

}

// encoding determine for html page
func determineEncoding(r io.Reader) encoding.Encoding {
	bytes, err := bufio.NewReader(r).Peek(1024)
	if err != nil {
		panic(err)
	}
	e, _, _ := charset.DetermineEncoding(bytes, "")
	return e
}
