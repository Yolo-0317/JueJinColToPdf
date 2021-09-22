import download
import mdToHtml
import subprocess
import json
import sys


def genPdf(title):
    # TODO:: 需要配置全局路径
    exePath = "wkhtmltopdf"
    sourcePath = "./htmls/%s.html" % title
    targetPath = "./pdfs/%s.pdf" % title
    cmd = '%s %s %s' % (
        exePath, sourcePath, targetPath)
    print(cmd)
    subprocess.run([exePath, sourcePath, targetPath])


def downloadAndGenPdf(cid):
    download.downloadColumn(cid)
    column = mdToHtml.getJSONData("./datas/%s/column.json" % cid)
    title = column["column_version"]["title"]
    print("开始生成html文件")
    mdToHtml.mdToHtml(cid, title)
    print("生成html文件完毕")
    print("开始生成%s.pdf" % title)
    genPdf(title)
    print("%s.pdf生成完毕" % title)


def downloadArticleAndGenPdf(aid):
    resArt = download.getArticleContent(aid)
    artContent = resArt["data"]
    folder = "./datas/%s" % aid
    download.ensureDir(folder)

    download.saveArticleContent(aid, aid,  json.dumps(artContent))
    download.saveArticleList(aid,  json.dumps([{
        "article_id": artContent["article_id"]
    }]))
    title = artContent["article_info"]["title"].replace(" ", "")
    print("开始生成html文件")
    mdToHtml.mdToHtml(aid, title)
    print("生成html文件完毕")
    print("开始生成%s.pdf" % title)
    genPdf(title)
    # print("%s.pdf生成完毕" % title)


C_ID = '6979380367216082957'
A_ID = '6991628964573741093'

# downloadAndGenPdf(C_ID)
# downloadArticleAndGenPdf("6991628964573741093")


def run():

    if len(sys.argv) < 2:
        return print("please input columnId or articleId");

    acid = sys.argv[1]
    actype = "c" if len(sys.argv) < 3 else sys.argv[2];

    print("acid:%s  acttype:%s" % (acid, actype));

    if actype == "a":
        downloadArticleAndGenPdf(acid)
    else:
        downloadAndGenPdf(acid)


run();
