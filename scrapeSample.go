package main

import (
    "fmt"
    "github.com/PuerkitoBio/goquery"
)

func main() {
    // 投稿した記事の一覧ページのリンクから、ドキュメントを取得
    doc, err := goquery.NewDocument("https://folio-sec.com/theme/virtual-reality")
    if err != nil {
        fmt.Println(err)
    }
    // 投稿した記事のリンクのurlを配列に格納
    var urls []string
    doc.Find(".title a").Each(func(_ int, s *goquery.Selection) {
        url, _ := s.Attr("href")
        urls = append(urls, url)
    })
    // 出力
    fmt.Println(urls)
}
