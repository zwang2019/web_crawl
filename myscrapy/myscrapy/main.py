from scrapy import cmdline


if __name__ == "__main__":

    cmd_args = "scrapy crawl douban".split()
    cmdline.execute(cmd_args)