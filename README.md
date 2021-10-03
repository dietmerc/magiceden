# MagicalEden - Monitor

## Installation :

    pip install -r requirements.txt

## Configuration :

**Edit : _config.json_**

Exemple :

```
{
    "collections": [
        {
            "collection": "<collection>",
            "price": 1,
            "webhooks": [
                {
                    "name": "<name>",
                    "url": "<url>",
                    "footer_name": "<footer_name>",
                    "footer_image_url": "<footer_image_url>"
                },
                {
                    "name": "<name>",
                    "url": "<url>",
                    "footer_name": "<footer_name>",
                    "footer_image_url": "<footer_image_url>"
                }
            ]
        },
        {
            "collection": "<collection>",
            "price": 1,
            "webhooks": [
                {
                    "name": "<name>",
                    "url": "<url>",
                    "footer_name": "<footer_name>",
                    "footer_image_url": "<footer_image_url>"
                },
                {
                    "name": "<name>",
                    "url": "<url>",
                    "footer_name": "<footer_name>",
                    "footer_image_url": "<footer_image_url>"
                }
            ]
        }
    ],
    "avatar_url": "https://pbs.twimg.com/profile_images/1444484250821087232/3zEbdU1R_400x400.jpg"
}
```

You can find collection name at the end of : https://magiceden.io/marketplace?collection_symbol=shroomz

#### Warning !

At the end of the last "}" or "]" do not put a ","

Exemple :

```
{
    "collections": [
        {
            "collection": "<collection>",
            "price": 1,
            "webhooks": [
                {
                    "name": "<name>",
                    "url": "<url>",
                    "footer_name": "<footer_name>",
                    "footer_image_url": "<footer_image_url>"
                } !!!
            ]
        } !!!
    ],
    "avatar_url": "https://pbs.twimg.com/profile_images/1444484250821087232/3zEbdU1R_400x400.jpg"
}
```

## Execution :

    python magicaleden.py
