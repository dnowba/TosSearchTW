from .tosneet_spider import TosneetSpider


class ItemsSpider(TosneetSpider):
    name = "items"
    start_urls = [
        'https://tos.neet.tv/items?f=1',
    ]

    def _parse_row(self, row, headers):
        data = super()._parse_row(row, headers)
        data['img'] = row.css('td img::attr(src)').extract_first()
        data['Grade'] = row.css('td .item-grade::attr(data-tip)').extract_first()
        return data
