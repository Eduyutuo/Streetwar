import urllib.request, json

url = 'https://api.github.com/repos/Eduyutuo/Streetwar/actions/runs/45273197341/jobs'
req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for j in data['jobs']:
            print(f"Job: {j['name']}, Status: {j['status']}, Conclusion: {j['conclusion']}")
            for s in j.get('steps', []):
                print(f"  Step: {s['name']} -> {s['conclusion']}")
except Exception as e:
    print('Error:', e)
