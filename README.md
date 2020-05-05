# Gossip-crawer
ptt 爬取 八卦版

## crawer_for_Gossiping.py 
### usage
```
python crawer_for_Gossiping.py start_page end_page
```
| Parameter | meaning | e.g. |
| -------- | -------- | -------- |
| start_page| 開始爬的頁數 | 30000 |
| end_page |  終止爬的頁數 | 30050|

最後生成 ```Gossip_title_start_page_to_end_page.csv``` 在同一目錄下

檔案格式:
|title|date|
|---|---| 

### example
```
python crawer_for_Gossiping.py 39000 39010
```
生成 ```Gossip_title_39000_to_39010.csv``` 在同一目錄下
