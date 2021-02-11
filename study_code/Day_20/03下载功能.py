import urllib.request

url = "https://cn.bing.com/images/search?view=detailV2&ccid=yBhYWLkI&id=F1DB9348301BF5A17B754AC61FAB5B13A5F6B31E&thid=OIP.yBhYWLkI228tPG4-T3vVaAHaKw&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fRc8185858b908db6f2d3c6e3e4f7bd568%3frik%3dHrP2pRNbqx%252fGSg%26riu%3dhttp%253a%252f%252ftu.jinvjie.com%252f30053003%252f1a9b5f852211081.jpg%26ehk%3dPFA8kJDga%252flu4R2rkZhYXPgWs43z4l4tQShERhVz49A%253d%26risl%3d%26pid%3dImgRaw&exph=1453&expw=1000&q=%e8%bf%90%e5%8a%a8%e7%be%8e%e5%a5%b3&simid=608045293895286928&ck=985FD7E2A9269E760154743FFA23DFAB&selectedIndex=0&FORM=IRPRST&ajaxhist=0"
path = "D:\\code\\py\\study_code\\Day_20\\1.jpg"

urllib.request.urlretrieve(url, path)  # 根据url下载到路径
