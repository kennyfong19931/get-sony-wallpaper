Download today's choice image from [Sony αcafe](https://acafe.msc.sony.jp/choice/list)

```
name: get-sony-wallpaper
services:
  npm:
    container_name: get-sony-wallpaper
    image: ghcr.io/kennyfong19931/get-sony-wallpaper:latest
    volumes:
      - /path/to/download:/download
```