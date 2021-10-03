import datetime
import requests
import threading
import time
import json

f = open('config.json',)
config = json.load(f)

OLD_NFTS = []
collections = config['collections']
avatar_url = config['avatar_url']


def delete_nft(NFT):
    global OLD_NFTS
    print("Deleting : " + NFT['title'] + " in 10 minutes")
    time.sleep(600)
    OLD_NFTS.remove(NFT)


def getDate():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def sendCode(name, price, img, nft_url, webhook_name, webhook_url, footer_name, footer_image_url, collection):
    data = {
        "embeds": [
            {
                "title": name,
                "description": "Price : " + price + " sol",
                "url": nft_url,
                "fields": [
                    {
                        "name": "Collection",
                        "value": "[" + collection + "]" + "(" + "https://magiceden.io/marketplace?collection_symbol=" + collection + ")"
                    }
                ],
                "thumbnail": {
                    "url": img
                },
                "footer": {
                    "text": footer_name + " | " + getDate(),
                    "icon_url": footer_image_url
                },
            }
        ],
        "username": "MagicalEden",
        "avatar_url": avatar_url
    }
    result = requests.post(webhook_url, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Webhook sent to : " + webhook_name)


def monitor(collection, price, webhooks):
    while True:
        response = requests.get(
            "https://api-mainnet.magiceden.io/rpc/getListedNFTsByQuery?q={\"$match\": {\"collectionSymbol\": \"" + collection + "\"}, \"$sort\": {\"takerAmount\": 1, \"createdAt\": -1}, \"$skip\": 0, \"$limit\": 500}")
        try:
            for NFTS in response.json()['results']:
                if NFTS['price'] <= price:
                    if NFTS not in OLD_NFTS:
                        OLD_NFTS.append(NFTS)
                        for webhook in webhooks:
                            sendCode(NFTS['title'], str(NFTS['price']), NFTS['img'], "https://magiceden.io/item-details/" +
                                     NFTS['mintAddress'], webhook['name'], webhook['url'], webhook['footer_name'], webhook['footer_image_url'], collection)
                        delete_nft_thread = threading.Thread(
                            target=delete_nft, args=(NFTS,))
                        delete_nft_thread.start()
        except json.decoder.JSONDecodeError:
            print("Can't reach MagicalEden.")


def main():
    for collection in collections:
        print("Monitoring : " + collection['collection'] +
              " <= " + str(collection['price']) + " sol")
        monitor_thread = threading.Thread(target=monitor, args=(
            collection['collection'], collection['price'], collection['webhooks'],))
        monitor_thread.start()


main()
