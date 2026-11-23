import urllib.request, json

url = 'https://api.github.com/repos/Eduyutuo/Streetwar/check-runs?check_suite_id=45273197341'
# Or list annotations on check run
req = urllib.request.Request('https://api.github.com/repos/Eduyutuo/Streetwar/actions/runs/45273197341/jobs', headers={'User-Agent': 'Python'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        job = data['jobs'][0]
        check_run_url = job.get('check_run_url')
        print("check_run_url:", check_run_url)
        if check_run_url:
            req2 = urllib.request.Request(check_run_url + '/annotations', headers={'User-Agent': 'Python'})
            with urllib.request.urlopen(req2) as resp2:
                ann = json.loads(resp2.read().decode('utf-8'))
                print("Annotations:", ann)
except Exception as e:
    print('Error:', e)
