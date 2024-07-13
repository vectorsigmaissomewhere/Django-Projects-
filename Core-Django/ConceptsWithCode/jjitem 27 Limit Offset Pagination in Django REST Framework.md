## LimitOffsetPagination

```text
This pagination style mirrors the syntax used when looking up multiple 
database records. The client includes both a "limit" and an "offset" query
paramter. The limit indicates the maximum number of itmes to return, and
is equivalent to the page_size in other styles. The offset indicates the 
starting position of the query in relation to the complete set of paginated 
items. 

To enable the LimitOffsetPagination style globally, use the following 
configuration:
```
