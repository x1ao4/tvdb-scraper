# tvdb-scraper
使用 tvdb-scraper 可以从 [TheTVDB](https://thetvdb.com/) 上抓取电视剧集的数据。它可以通过与 TheTVDB 网站进行交互，获取指定电视剧的剧集信息，包括剧集的季数、集数、播出日期、时长和剧集标题等，还可以选择下载对应的封面图片。

## 示例
假设您需要获取「人生切割术 第一季」的剧集信息，使用 tvdb-scraper 后，你会得到以下数据：
```
1;2022/2/18;57;Good News About Hell
2;2022/2/18;53;Half Loop
3;2022/2/25;56;In Perpetuity
4;2022/3/4;46;The You You Are
5;2022/3/11;43;The Grim Barbarity of Optics and Design
6;2022/3/18;40;Hide and Seek
7;2022/3/25;49;Defiant Jazz
8;2022/4/1;46;What’s for Dinner?
9;2022/4/8;40;The We We Are
```

## 运行条件
- 安装了 Python 3.0 或更高版本。
- 安装了必要的第三方库：requests、lxml 和 datetime。

## 使用方法
1. 将仓库克隆或下载到计算机上的一个目录中。
2. 根据需要，修改脚本中的参数：series_id、start_season、end_season 和 download_covers。
   - series_id：电视剧的 ID，您可以通过电视剧在 TheTVDB 的网页地址（例如：`https://thetvdb.com/series/ID`）获取 ID。
   - start_season：要获取信息的起始季数。
   - end_season：要获取信息的结束季数。
   - download_covers：是否下载封面图片（True 表示下载，False 表示不下载）。
     
   注：当 `start_season = 0` 且 `end_season = 4` 时，表示会获取第 0、1、2、3、4 季的剧集信息，若只需要获取某一季的信息，给 start_season 和 end_season 赋予相同的季数值即可。
3. 修改 `start.command (Mac)` 或 `start.bat (Win)` 中的路径，以指向您存放 `tvdb-scraper.py` 脚本的目录。
4. 双击运行 `start.command` 或 `start.bat` 脚本以执行 `tvdb-scraper.py` 脚本。
5. 脚本将开始获取指定剧集的信息和封面图片（如果选择下载），并将结果写入到同一目录下以电视剧 ID 为名的文件夹内。脚本会为每一季创建一个名为 `S{season_number}-{episode_count}.txt` 的文件用于存储该季的剧集信息，如果您选择下载封面图片，脚本还会创建一个名为 `S{season_number}-{episode_count}` 的文件夹，用于存储该季每集的封面图片。

## 注意事项
- 如果脚本无法连接到 TheTVDB 网站，请检查您的网络连接，并确保网站可以访问。
- 如果需要下载封面图片，请确保您的工作目录具有足够的存储空间。
<br>

# tvdb-scraper
With tvdb-scraper, you can scrape TV show data from [TheTVDB](https://thetvdb.com/). It can interact with TheTVDB website to obtain information about specified TV shows, including season number, episode number, air date, duration, and episode title. You can also choose to download the corresponding cover images.

## Example
Suppose you need to get information about the first season of “Severance”. After using tvdb-scraper, you will get the following data:
```
1;2022/2/18;57;Good News About Hell
2;2022/2/18;53;Half Loop
3;2022/2/25;56;In Perpetuity
4;2022/3/4;46;The You You Are
5;2022/3/11;43;The Grim Barbarity of Optics and Design
6;2022/3/18;40;Hide and Seek
7;2022/3/25;49;Defiant Jazz
8;2022/4/1;46;What’s for Dinner?
9;2022/4/8;40;The We We Are
```

## Requirements
- Python 3.0 or higher is installed.
- The necessary third-party libraries are installed: requests, lxml, and datetime.

## Usage
1. Clone or download the repository to a directory on your computer.
2. Modify the parameters in the script as needed: series_id, start_season, end_season, and download_covers.
   - series_id: The ID of the TV show. You can get the ID from the TV show’s web address on TheTVDB (e.g., `https://thetvdb.com/series/ID`).
   - start_season: The starting season number to retrieve information for.
   - end_season: The ending season number to retrieve information for.
   - download_covers: Whether to download cover images (True means download, False means do not download).
     
   Note: When `start_season = 0` and `end_season = 4`, it means that information for seasons 0, 1, 2, 3, and 4 will be retrieved. If you only need to retrieve information for a single season, assign the same season number value to start_season and end_season.
3. Modify the path in `start.command (Mac)` or `start.bat (Win)` to point to the directory where you store the `tvdb-scraper.py` script.
4. Double-click `start.command` or `start.bat` to execute the `tvdb-scraper.py` script.
5. The script will start retrieving information and cover images (if selected) for the specified TV show and write the results to a folder with the same name as the TV show ID in the same directory. The script will create a file named `S{season_number}-{episode_count}.txt` for each season to store information about that season’s episodes. If you choose to download cover images, the script will also create a folder named `S{season_number}-{episode_count}` to store cover images for each episode of that season.

## Notes
- If the script is unable to connect to TheTVDB website, check your network connection and make sure the website is accessible.
- If you need to download cover images, make sure your working directory has enough storage space.
