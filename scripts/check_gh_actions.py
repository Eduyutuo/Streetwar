import urllib.request, json

url = 'https://api.github.com/repos/Eduyutuo/Streetwar/actions/runs?per_page=5'
req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print(f"Total workflow runs: {data['total_count']}")
        for r in data['workflow_runs']:
            print(f"Run ID: {r['id']}, Status: {r['status']}, Conclusion: {r['conclusion']}, SHA: {r['head_sha'][:7]}, Name: {r['name']}")
except Exception as e:
    print('Error:', e)
