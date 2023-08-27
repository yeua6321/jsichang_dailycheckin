import http.client

conn = http.client.HTTPSConnection("panel.skynode.pro")

payload = "{\"g-recaptcha-response\":\"03ADUVZwAboO-J7ytCi-YTaTRdckcN2P0mIRkMV_LwHDwtEX25EYZt2dBwOejJbe3FyF1707HmiCxYbZkhmt5aIwLV5lppK235EAG9U3LsLuSGGWKGXOOvPP4lA72h5xCma-oSR_B5Cjh_XXb8wRtNGXdR-2xAHYTxfOnTYlMbPouzXd4ddtBTr3KBlmmTqsaD69GPGF0DoUVCMl4lBz40bGql0kmpyc5pf6l1pvKbM-dEKBIyFBPOLmZDCpwQySV4iRAf9knAbg8b7_DC1Q3NNk9651Bj2zuvrIjfe4iSgiXl1UdSuAiA_tGNoEYsrUJVYTlw9jV4MueNzI5uXKUmuiy67CJiuKofghkPCxYJ023PMzqlHJQ8b2-c_yFFWwGya23_kjrHFzWvxlzYd25DVh-hg_817DyVgY_HQamNWgxrr6PS0euTMTcHs9SO3ZIXN2NfI3EnOOkmctJyy0cMLu3pAbuMLR_gMdL5hsPNeKCwHj11sznxgkh__Zfr8oRgHsFpajLv6t9a-ajnIeie4q7hnmn1vsPB0Rn88VeHJoMGYvpxOYgM63C60UYvfpnSU85R5Vvgth8o\"}"

headers = {
    'cookie': "_gid=GA1.2.1287579901.1693154354; _gcl_au=1.1.1191558003.1693154456; crisp-client%252Fsession%252F598ecbd2-b24c-4d30-a9e1-c188f2342e7d=session_57901561-4ede-4e8e-a433-d480b9954694; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlJFK1dIZndlQlRzLzR4amtSaE9NM3c9PSIsInZhbHVlIjoiRmw1Nm5xdlZOSU15SllOMldTb1FJeGYxOVlmd21DNWN0eUc2MFR4QnVucDhKK05DTVRuTTZQWi9TZ3RndDRIaGI3aFF2a0FOMVhMdVg3QlAxRnBoanJmQTZFNWwydGFZMFB2cmNNMmlIQmJldmRiQ29KQThJS3ExWVR2NThreVRldzZDdmRsMGhGcG9oU3JlOGhmbXBJbHhIaWNKYTBnZk9scUhsbkxnRm1QOTQ4Qjk0T3BheHQrQldWKyt3d0pydGdQZWRna1NkOUZaMDRwT0FyME8rNjZROEtEWFI5eWtQQXhqbUVjbjV3WT0iLCJtYWMiOiJhMzljY2UyNWNiZmEwYTdkMTcxMTBkNzA1YzUzYmEyY2E0OTYzY2UwZTI1OGIxNjk1OGNmZGIxODY3ZDhhMDEwIiwidGFnIjoiIn0%253D; cto_bundle=GXQO7V9CVFpHYTBKZGVDUSUyQklidXJIVHN3ZUZoYkI5azVaM0ZmZVpGdjZMYVBMS0hxM0pzbWNvU1IzWnd2SCUyQjUxRUp3WE1wMkdHSFFUOGpVbmJxbmhGRWRlNjNjdyUyQkVnTWdiZUs2SzJvVFNuNkQlMkI4YXQ2YkZRZHVITUxnUzdjQkxQU2djeHpDQ1p0SGV4dFJiTVFnZjB0R0Y0USUzRCUzRA; _ga=GA1.1.1936097813.1693154354; cf_clearance=4gSJoW0VrrAQX.0YspjVEfVKLXmDEp6Y5vPRdeB_qeA-1693168902-0-1-6cbdea28.2ed7da1b.cd7b963b-0.2.1693168902; XSRF-TOKEN=eyJpdiI6IjBGKzVncWk1VWpJRmpzckh1VU9BWWc9PSIsInZhbHVlIjoidWl4MmF2TE5iSVQwbk1sUE9Mc2hITHF3elZyTkV2UVR5V1RCenJmeHN5bk1uelZZRjFTUHd3WXJZRVFiZlhmWityeXhzOWZrd0RDSFZWQk9mTkRGY1QrRHJ0ZlRpWmJTY0x0ZXVzQkVjVmNEN205a0J0UUlxU2FPUnpwTFZKRTMiLCJtYWMiOiJiNDIwOTYxNWU1NTk0YWEzODlkY2I3ZmNmZjc1ZGY3YTc2ZTlkYzM0ZDhiYjY3ZTQ1YTg3OWJjZjcxOGU1NmFmIiwidGFnIjoiIn0%253D; pterodactyl_session=eyJpdiI6ImQ5Ym1GU2xON3FDR0hadDZIZngrNkE9PSIsInZhbHVlIjoiNysyUUZPZ1hlOHpWNmdDckVTZVdMbUlEbEtWVW9wMUk1TW5TL0FUYm8xYzViWDM2Ym5oKzVESlk2RnhkdmJ6OTlvNUFFb0dRN0t1dE5ybE93RXBqZStJK0ZScU5kM0V3ZFZjSGJWWVY5UjUyWVVkNUFhMlVtOExtUVFkblB4cDgiLCJtYWMiOiJiYmVmZDc2ZGQzZDM2OGNlOTA5N2Y4MmZkNjY0ZGY5M2Y0ZDJmYTkxNDYxMWZiMWJhNGZjMjgyNWRmMDU0YzBiIiwidGFnIjoiIn0%253D; __gads=ID%3Dab8645a6a44a24b3%3AT%3D1693154555%3ART%3D1693168983%3AS%3DALNI_MaLDvOmqCVs4LN0ieP-eAheJFvxag; __gpi=UID%3D00000c34e266d092%3AT%3D1693154555%3ART%3D1693168983%3AS%3DALNI_MYe0jH_kGdRK3h0iMUOgNFYvq7x6g; _ga_ZKPWHEDKB0=GS1.1.1693166089.3.1.1693169010.60.0.0",
    'authority': "panel.skynode.pro",
    'accept': "application/json",
    'accept-language': "zh-CN,zh;q=0.9",
    'content-type': "application/json",
    'origin': "https://panel.skynode.pro",
    'referer': "https://panel.skynode.pro/server/1c121cf5/console",
    'sec-ch-ua': "" Not A;Brand";v="99", "Chromium";v="102"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': ""Windows"",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'x-xsrf-token': "eyJpdiI6IjBGKzVncWk1VWpJRmpzckh1VU9BWWc9PSIsInZhbHVlIjoidWl4MmF2TE5iSVQwbk1sUE9Mc2hITHF3elZyTkV2UVR5V1RCenJmeHN5bk1uelZZRjFTUHd3WXJZRVFiZlhmWityeXhzOWZrd0RDSFZWQk9mTkRGY1QrRHJ0ZlRpWmJTY0x0ZXVzQkVjVmNEN205a0J0UUlxU2FPUnpwTFZKRTMiLCJtYWMiOiJiNDIwOTYxNWU1NTk0YWEzODlkY2I3ZmNmZjc1ZGY3YTc2ZTlkYzM0ZDhiYjY3ZTQ1YTg3OWJjZjcxOGU1NmFmIiwidGFnIjoiIn0="
    }

conn.request("POST", "/api/client/servers/1c121cf5-e70c-4a82-a2e8-b5eb6cbeffee/renew", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
