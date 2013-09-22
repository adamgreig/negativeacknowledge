import re
import sys
import glob
import requests

FLICKR_API_URL = "http://api.flickr.com/services/rest/"
FLICKR_API_URL += "?method=flickr.photos.getInfo&format=json&nojsoncallback=1"
FLICKR_API_URL += "&api_key="
FLICKR_API_URL += sys.argv[1].strip()
FLICKR_API_URL += "&photo_id="

FLICKR_PHOTO_URL = "http://farm{farm}.staticflickr.com/"
FLICKR_PHOTO_URL += "{server}/{photo}_{secret}_z.jpg"

IMG_TAG = '<a href="{flickr_url}" title="{title}">'
IMG_TAG += '<img src="{url}" alt="{title}" /></a>'

RE = re.compile(r'\[flickr p?id="(\d+)".*?\]', re.DOTALL)

for post in glob.glob("*.md"):
    with open(post) as f:
        print("Opening {0}...".format(post))
        contents = f.read()

    replacements = []
    for match in RE.finditer(contents):
        photo = match.group(1)
        print("Requesting URL for photo {0}".format(photo))
        url = FLICKR_API_URL + photo
        r = requests.get(url)
        image = r.json()['photo']
        print("Image JSON: {0}".format(image))
        secret = image['secret']
        server = image['server']
        farm = image['farm']
        title = image['title']['_content']
        flickr_url = image['urls']['url'][0]['_content']  # omg flickr
        url = FLICKR_PHOTO_URL.format(farm=farm, server=server,
                                      photo=photo, secret=secret)
        print("Got URL: {0}".format(url))
        tag = IMG_TAG.format(flickr_url=flickr_url, url=url, title=title)
        replacements.append((match.span(), tag))

    if not replacements:
        print("No matches found, continuing...")
        continue

    newcontents = contents[:replacements[0][0][0]]
    for idx in range(len(replacements) - 1):
        newcontents += replacements[idx][1]
        newcontents += contents[replacements[idx][0][1]:
                                replacements[idx + 1][0][0]]
    newcontents += replacements[-1][1]
    newcontents += contents[replacements[-1][0][1]:]

    print("Replacing contents...")
    with open(post, "w") as f:
        f.write(newcontents)
