# Final version supplied by:
# https://github.com/ricco386/Udacity-CS101/blob/master/crawler.py


def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed): # returns index, graph of outlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>:[list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            if page in graph:
                graph[page].append(outlinks)
            else:
                graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])


def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None


def add_page_to_index(index,url,content):
    content_list = content.split()
    for word in content_list:
        add_to_index(index,word,url)


def record_user_click(index,keyword,url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] += 1


def compute_ranks(graph):
    d = 0.8 #dumping constant
    numloops = 40

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            #Loop throught all pages
            for node in graph:
                #check if node links to page
                if page in graph[node]:
                    #Add to new rank based on this node
                    newrank += d * ranks[node] / len(graph[node])
            newranks[page] = newrank
        ranks = newranks
    return ranks


def lucky_search(index, ranks, keyword):
    result = ''
    if not keyword in index:
        return None
    else:
        for url in index[keyword]:
