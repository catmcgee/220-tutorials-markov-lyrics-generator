import re #REGEX library
import urllib.request #Open URLs
import markovify #Generate a Markov chain

#Find all links on an artist's AZLyrics page
originalLyrics = open('lyrics.txt', 'w')
url = "https://www.azlyrics.com/c/coldplay.html"
artistHtml = urllib.request.urlopen(url)
artistHtmlStr = str(artistHtml.read())
links = re.findall('href="([^"]+)"', artistHtmlStr)

#Ensure they are lyrics links and add them to a new list
songLinks = []
for x in links:
    if "lyrics/coldplay" in x:
        x = x.replace("..", "")
        x = "https://www.azlyrics.com/" + x #The links were missing the beginning of the URL, so we add them before appending
        songLinks.append(x)

#Get the HTML from the lyrics pages
for x in songLinks:
    songHtml = urllib.request.urlopen(x)
    songHtmlStr = str(songHtml.read()) 
    #Split the HTML string twice so that we only get the lyrics
    split = songHtmlStr.split('content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->',1)
    split_html = split[1]
    split = split_html.split('</div>',1)
    lyrics = split[0]
    #Replace the HTML of the lyrics we don't want
    lyrics = lyrics.replace('<br>', '\n')
    lyrics = lyrics.replace('\\', '')
    lyrics = lyrics.replace('\nn', '\n')
    lyrics = lyrics.replace('<i>', '')
    lyrics = lyrics.replace('</i>', '')
    lyrics = lyrics.replace('[Chorus]', '')
    originalLyrics.write(lyrics)
originalLyrics.close() #We close the file because we no longer have to write anything to it

#Generate new lyrics using a Markov Chain
generatedlyrics = ()
file = open('lyrics.txt', 'r') 
text = file.read()
markovifyTextModel = markovify.Text(text)
generatedlyrics = markovifyTextModel.make_sentence() #This is only one of Markovify's capabilities
print(generatedlyrics)

#You can do some awesome things with the new generatedlyrics variable. Check out the blog post for ideas.



   
