from datetime import datetime
from lxml import html
import os
import requests

series_id = 'demon-slayer-kimetsu-no-yaiba'
start_season = 0
end_season = 4
download_covers = True

base_url = 'https://thetvdb.com'
series_url = f'{base_url}/series/{series_id}'

if not os.path.exists(series_id):
    os.makedirs(series_id)

print(f'Current working directory: {os.getcwd()}')
print()

info_count = 0
cover_count = 0
failed_info = 0
failed_cover = 0

for season_number in range(start_season, end_season + 1):
    success = False
    attempts = 0
    while not success and attempts < 3:
        try:
            season_url = series_url + f'/seasons/official/{season_number}'
            response = requests.get(season_url)
            tree = html.fromstring(response.text)

            print(f'Ready to process season {season_number}')
            print()

            episodes = tree.xpath('//*[@id="episodes"]/table/tbody/tr')
            episode_count = len(episodes)

            season_filename = f'S{season_number}-{episode_count}.txt'
            season_covers_dir = f'{series_id}/{season_filename[:-4]}'

            if download_covers and not os.path.exists(season_covers_dir):
                os.makedirs(season_covers_dir)

            with open(f'{series_id}/{season_filename}', 'w') as f:
                for i, episode in enumerate(episodes, 1):
                    try:
                        episode_number = f'{i}'
                        air_date = episode.xpath('td[3]/div[1]/text()')[0].strip()
                        air_date = datetime.strptime(air_date, '%B %d, %Y').strftime('%Y/%m/%d')
                        duration = episode.xpath('td[4]/text()')[0].strip()
                        episode_title = episode.xpath('td[2]/a/text()')[0].strip()
                        f.write(f'{episode_number};{air_date};{duration};{episode_title}\n')
                        print(f'Processing season {season_number} episode {i}: {episode_title}')
                        info_count += 1
                    except IndexError:
                        failed_info += 1
                        print(f'Failed to save info for season {season_number} episode {i}: {episode_title} - Content not found')
                    except requests.exceptions.RequestException:
                        failed_info += 1
                        print(f'Failed to save info for season {season_number} episode {i}: {episode_title} - Connection error')
                    except Exception as e:
                        failed_info += 1
                        print(f'Failed to save info for season {season_number} episode {i}: {episode_title} - Unknown error')

                    if download_covers:
                        success_cover = False
                        attempts_cover = 0
                        while not success_cover and attempts_cover < 3:
                            try:
                                episode_url = base_url + episode.xpath('td[2]/a/@href')[0].strip()
                                response = requests.get(episode_url)
                                tree = html.fromstring(response.text)
                                cover_url = tree.xpath('//*[@id="app"]/div[3]/div[3]/div[1]/a/img/@src')[0]
                                response = requests.get(cover_url)
                                cover_data = response.content
                                cover_filename = f'{episode_number}.jpg'
                                with open(f'{season_covers_dir}/{cover_filename}', 'wb') as cover_file:
                                    cover_file.write(cover_data)
                                cover_count += 1
                                success_cover = True
                            except IndexError:
                                attempts_cover += 1
                                if attempts_cover == 3:
                                    failed_cover += 1
                                    print(f'Failed to download cover for season {season_number} episode {i}: {episode_title} - Cover image not found')
                            except requests.exceptions.RequestException:
                                attempts_cover += 1
                                if attempts_cover == 3:
                                    failed_cover += 1
                                    print(f'Failed to download cover for season {season_number} episode {i}: {episode_title} - Connection error')
                            except Exception as e:
                                attempts_cover += 1
                                if attempts_cover == 3:
                                    failed_cover += 1
                                    print(f'Failed to download cover for season {season_number} episode {i}: {episode_title} - Unknown error')
            success = True
        except Exception as e:
            attempts += 1
            if attempts == 3:
                print(f'Season error: Failed to connect to thetvdb.com')
    print()

print(f'Episodes saved: {info_count}')
print(f'Covers saved: {cover_count}')
if failed_info > 0:
    print(f'Episodes failed: {failed_info}')
if failed_cover > 0:
    print(f'Covers failed: {failed_cover}')
