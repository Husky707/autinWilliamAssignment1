import newspaper
import sys

def extract_article(article):
    article.download()
    article.parse()
    article.nlp()

def write_info(article):
    info = article.title + "  -  " + ", ".join(article.authors) + '\r\n' + article.summary + '\r\n'

    #print(info)
    try:
        fileStream.write(info)
    except:
        print('Could not find "news_summary.txt" to write to.' + "\n")
        printData = input("Press 0 to print info to the command line or 1 to abbort")
        if printData == "0":
           print(info)
        else:
            exit("Scrapping aborted")
            fileStream.close()

def scrape_sites(siteList, iscashed = False):
    for eachSite in siteList:
       scrapedSite = newspaper.build(eachSite, memoize_articles = iscashed)
       for article in scrapedSite.articles:
         extract_article(article)
         if (keyIn == "" or has_keyword(article) == True) & (has_author(article)) :
             write_info(article)

def has_keyword(article):
    for eachKey in article.keywords:
        if eachKey.lower() == keyIn.lower():
            return True

    return False

def has_author(article):
    if authIn == "":
        return True

    for eachAuth in article.authors:
        #print(eachAuth)
        if eachAuth == authIn:
            return True
    return False


if __name__ == '__main__':

    fileStream = open('news_summary.txt', 'w')


    keyIn = input("Please enter any keyword(press enter to continue):")
    authIn = input("Enter an author's name to refine search(name as listed in publication)" + "\n")
    print("Processing...")
    sites = ['https://www.gamespot.com/news/', 'https://www.gamesradar.com/news/', 'https://spikeybits.com/']
    scrape_sites(sites)

    print('Scrapping Complete')
    fileStream.close()

