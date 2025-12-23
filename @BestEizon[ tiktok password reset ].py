print('I can make any tool for requests / telegram @besteizon')
import requests
import json
import webbrowser
webbrowser.open("https://t.me/eizonxtool")
def xor(value: str) -> str:
    return "".join([hex(ord(_) ^ 5)[2:] for _ in value])


cookies = {
    'cookie-consent': '{%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}',
    'delay_guest_mode_vid': '5',
    'passport_csrf_token': '9d53769d80f567f59f26026d80a350d7',
    'passport_csrf_token_default': '9d53769d80f567f59f26026d80a350d7',
    '_ttp': '35UIHOLpZW6QuGGXamMrj2oRjkD',
    'tiktok_webapp_theme_source': 'auto',
    'tiktok_webapp_theme': 'dark',
    'tt_chain_token': 'OrbNqTRmtOX1/5E8EVDiyw==',
    'd_ticket': 'f7251423ac19813301938b436f6f6578de1da',
    'tt_csrf_token': 'lymRYBqu-JlTsfFFKo8njr0YFCDgJZZsiY00',
    'multi_sids': '6601726223641722886%3Aa4db5dbb28b255eeb1db6e4c881c3b83',
    'store-country-sign': 'MEIEDHFUHGr2TlHFNmRYUwQg9nmWeli5wuRFTdR3Yx1pDeVKcqWM1mzcYdMjKTUs_qIEECyy0LxZjfNj8V5LUNMimDM',
    'sid_guard': 'a5de695249a843a427c233a6452cd060%7C1766502965%7C21599%7CTue%2C+23-Dec-2025+21%3A16%3A04+GMT',
    'uid_tt': '7bfe14d4da2f149aaac2d6a6678cc71a',
    'uid_tt_ss': '7bfe14d4da2f149aaac2d6a6678cc71a',
    'sid_tt': 'a5de695249a843a427c233a6452cd060',
    'sessionid': 'a5de695249a843a427c233a6452cd060',
    'sessionid_ss': 'a5de695249a843a427c233a6452cd060',
    'tt_session_tlb_tag': 'sttt%7C4%7Cpd5pUkmoQ6QnwjOmRSzQYP________-_k853GYjiRCmG4XqFrLFbBjSJjYI40Pj1JFKTMe_Y5u8%3D',
    'sid_ucp_v1': '1.0.1-KGUwM2Y4MDkyZTBhMzY3NDNmMmJjMjkzOWNiYmVmZDNhNzY2NjM1ZjkKCRC15KrKBhizCxADGgJteSIgYTVkZTY5NTI0OWE4NDNhNDI3YzIzM2E2NDUyY2QwNjAyTgog9rDnM7gBwl7qwksXKTLJP86JKutGIYFriCajpzhdW6ISII_GGPz4WHcKE2rmC35z7R9dNpSE_QJm8LAYJuvh-ZoJGAUiBnRpa3Rvaw',
    'ssid_ucp_v1': '1.0.1-KGUwM2Y4MDkyZTBhMzY3NDNmMmJjMjkzOWNiYmVmZDNhNzY2NjM1ZjkKCRC15KrKBhizCxADGgJteSIgYTVkZTY5NTI0OWE4NDNhNDI3YzIzM2E2NDUyY2QwNjAyTgog9rDnM7gBwl7qwksXKTLJP86JKutGIYFriCajpzhdW6ISII_GGPz4WHcKE2rmC35z7R9dNpSE_QJm8LAYJuvh-ZoJGAUiBnRpa3Rvaw',
    'ttwid': '1%7CV_v-HnvQY8gIUL8D1FMozAyjQWijbIYzrCP2q4okzrM%7C1766503028%7Caf268c6e621a809139cd1bfdebe77ffc6a630bddf588112958307e8ff235ba5d',
    'odin_tt': '0a814d431e934cdf72bfc10d232fe70ad82b53cf1e190e2d28d8ded612fd78dc823323462102e1ace5c8d041edf5cff6635aa1c6ca9be075ac2dd1240739f7c447d50a0c8ca7a5003783474db72f7fce',
    's_v_web_id': 'verify_mjiqefn2_MhPVrcLn_vbvN_4QbO_BZwh_xL997annY2Qu',
    'msToken': 'rA83Eb2XH7CDj_vBOCqzOQ5jG8FGoomtsxFagGQCpjlAsB_S6d96uratTlhQ-A6GlwkCIjGYUwuO6Guwlc3sgxEBVSGS_BpnyfLTAIZdcy-vyGZYwmoiVU_X8Sw47yabhmNYwz9h1I3jmFM=',
}


headers_send = {
    'accept': 'application/json, text/javascript',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.tiktok.com',
    'priority': 'u=1, i',
    'referer': 'https://www.tiktok.com/',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'tt-ticket-guard-client-data': 'eyJ0c19zaWduIjoidHMuMS5mYmM1M2Q1N2I0MzhmNDJkNmYzZmZiYWRhOWVhYmZkYWZiNjZmZGZkMjllNjhmM2ZhODhiMTAyMDBjMjgzY2NjMGU3MGI0YmRhODJjMTM4MzZlNWNmYTE4Mzk0ZDcwMjQwZjhhZjE2MzFmMTY1YWU5NjAxMjJlZWZmZDQ1MzNkZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJNRVVDSUNZd2NGd0dPSzZhQVJGbWdET0pJbEVHMHJhYWZnTVI4WCsxOEF4WVV5dy9BaUVBcy9nV1duY0t1QnhZemw3WlNkeFdHUy92KzIvT1ZGUVYvdjJtMDk3akp4Yz0iLCJ0aW1lc3RhbXAiOjE3NjY1MDMyMDl9',
    'tt-ticket-guard-iteration-version': '0',
    'tt-ticket-guard-public-key': 'BDgmkQJtdgPcyB0MOVdCwWRZzCSuzRxWi5znJUxjRC98hjzw7rI8J665DJEt41sHl4T4rr0MVtyd3A3UqAtQ+EQ=',
    'tt-ticket-guard-version': '2',
    'tt-ticket-guard-web-version': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-mssdk-info': 'V42ze1bgxBvmwAH0FWlryRH0qw9BJTtPsK6yTm.hzABvPRKycAZBlj0cBITp8fjDPdRuSpxlAFEaqGYLJoBFGBsJ0VJ93ModUzCpHIO52UKMj6onLVEHDYNlv4wlTc4EpovAxOM6qvA0qlWAa714aUDrHISRxuZvSczsX9rlp8.V8yb-9nJjD.C4O5YfBqHM8kBe6rRVfpakqYQb5sefzLnIZlpmjmkLkXK5hkS.YC3VfRPMK-7mhXduSyt66XZ7c02T9Xnf2cIBO.5FxTNsZSqfv13aaGdin31ZQVdDol8oCTXy-aNjlYdIAilBIDFSoN1-MvjYqwp0GYyMa1.PoV0vbRNXbRnUvNwGpqtOsAQ4Uzzbit5UddR-nK5a2pDUfw0qxzjwpkKG04qnIjK9sBsdEMQIHznsH8jRBIUBs-FFYJRyFhI033Ka2H7bToy6IhzljraMOTtVAGL8QEuaykZ.R1j-vmgzrjZbkml0r4AOg-0RSqjE.UczcZxtovLHnfFxhrKMkhbFvtEovx7fmrz7B2AndeBzHAXQTaQ9f7gQIRVXjlyqAKOl9wO2IikUCBbMQMlreQVQ18Q5vCsrvAURlaM9sCCmMFyJlj-itOWplLjF-JSC9D9JAnFZEPcu2DkxUd4KbCbAJF3WE.WLHUBqDlbt9aHei..LR5gygtduyihUDpxglHukfagYy6uLcYOIEXXsV89zFW7GLI71sLauzetDC4uUvRwZ9vRZbzrC9dWebBZHxJq9pF.UGXfupcNV5CSsM72VZ3RNmbAhEV9ltJNKmGZY82U-sac-Z3Rjul9QqoWqpfzbKPCoGR6d1KEYpCwxeXPwM2Za3W8SIn0bx7cc15kZl-HQdPpzgXlaiLvhRqgUF5gGiemA7wQJ0s6G2Q4quKbioCE5VwhlVGqwtf2GR5o37glMxtEQn79KYKmFe0ke0Dbvw5oTUKDjbX3nxEoF5A2NXpcxTHLjDnsbasRdQthqhMxgiwphKEcbw-DsmX1gnwH-Y4FwV2bYkzouj96XFO1xT7QSGET2jd379xnibWnayP4ZC1ikbrLPus5EmRZuE5jcl7db1nP7MrYber4fCBdjL7MGb.Wt0MIhROUAJiM14k3pb8KN.PMklpcHMO4AUUElhahG2ZVybUX-sVt-F8Ez5yANy0gD.KKSM9PW2DMWIilWz48lt6rY-I3FX5b184iMexpO2rvTbGFRNroVcAwcEqQu0iMB7BrSeKzMPUJG22oxK0EJGT5VhM2mNUl9m9HamnfvDAOEz9ig-q7dxBkif-l6cgxcD-v0l6xw442snk1e6i7fkOFQZoeGRRLtb1g2-ffFjd41zt57cZ13TcqMNjcX4bsHXApCscD2pOVxUHZGTKUiPNUegp4cwIf0XIyipcYFl1IaLiaoG5QYBAhDzUUoz8.WaBUUa5n-t5Ci14dggjx6nJBA6gsF5LXLs-OCQB9Tft9KmI-Juarn2dOcWd7uM5hgZdLCzCPoLzNRVz1xhR0uWnFPPM04hpgklyWqqoM2NaRDUqhJxBKYQAs.KUcs7GXrccqjffZpERO0V9u8Qit0FC0jZsyR-iW-kAWB0G8rfHw.0igFkZTfh0mku6K1jf8LdoLEWBWzh62CRrNnGvPakZJn08VSsb-xv28ujsJ3ngLxqEuL5zdVnHytSxcTJOMyyo4yUBb3w.XWA.ntCZfcsyhwAc4ghx0pBVX-rhu2re9tVi0fHGsTnK0p9b5DrSvdE1x4jZoMWOMJijTvHYeqMrb8GxD4Ej63rErRCnCruIuUoGqu12DeONel.JEoX2Zd5pIkFrB7Ieo.8Zr9ezOjW6FwUhsrXn5Mmkgp7ReloWwTl4ZHbuTwG4nefgU0NXfA2LTleP6PJirralB21jYLcWweAxTi-U40BBGw.Ug7sIGMeQBnlLL9kxpGJcXEoFwSj-U9f4xAWh8OnBPop0R88xqNc7ui2u6BHOTOXYR1FfPI0yMPcKq9u2g3C4IhHiG5K1ehCNSGkJ5zH9UH2S7P4uE7Sypa4KIoJct6iYy3MtTMBv1MDERmQygr7rCqYhB4Fi8bIhVFF5qyLGoILneZUIwM8Usb7V8.7c0jXkNL60-we0q1SInjfaVZxVhjV0qNCJkpnFI.tW50k8yuFLG9DHv7pakaV5V-rcfD6eQhpa09HwIeNRtxlyxY-qvXYTBSysxdSCBx2qtaZaX.6eOetJOpfpTxJmgRpVPRXzuGikyKePBp77pC4Ib3XCpPI25DxPZC3swZ83wYoROPrN-z50AEnADSjn.EJlCci0Hpd5DbRd9yDbcRl5xgskJAgfiASJxKGUsblq5Nkj8q1Rp8nmnTJ9XYr4u1c-gCROKI1qKvZkCsRdgv72G-BdHnCa-NHXU0qJY0MlfCNmBw5nKW2IuyumOhqAP5rWN0Re.d4YSEDLjCVrQT6NxtX0aGGjdQUZI4S-X7zWI7iLIPjjkd7Zp-ZMxtBA7qgJ1HzChwX55mzMtNnRiAXvYdZoYcIIhCxl9Ah0FffxEmPokTVQejoFFlk1loFuKzo5J0lCGPNwQZggvEnU4nbuo1Qpj0mO9AQY6ZpUjkhfbFV9oK46RmMQSL0j.LTQw1Fqw1nqdJvr5PJZ5o5U7MCBaHTXrU.Dq3MHpCmaqCkIRm91dGFnM5IFP50-ALn4q-utLscsago359RWmziv7Gw-yvuqYbaGg72G7Giy.zZkn6h0ha2s1HHJ0AFnFWrlBNlPiANYaHU4YLVim.kDs.Am-8F1xK-9znhgaoHU-WWnKFlzJ5Qtbf57rxeo7lxAuweAY76WAEIuBc9V2ATLmt8lJJOHXXmjuJj.ZTQr7ABaiySaAoVwM9EbTCq-s4dEADf1sPrh1ttMfxo2W8GesCHCDCK1LL3tSdyq3hOkPAlEhmyoTjqrqjqaMVQp9WdQAiucdlK3ZDE2KMjKEGupSWJiSPIywzonV1FKgZYj13QX1FkKQ7.67joxUahRDv5-6EA7WqhHuDJaOxDVRoxF59c107wm087sCgfvwpKZkzGM29-aTF4gAyI2HTyPoJSXNrOSKoSuoBYiDFgCyi1ln-aHUxTp2yiA6.OnE43wNRyGD0FM4VR9IHwtSTE-1DCP9X60K9gzaVOd3tiybH9taZsLlYDe3zkDIDoSIECXggfgoFQ1wVfiFkQ0nZuHXBmC5NrSNFi.aZHO8uDv.mxrHEEhKWKwtnByVg6Sb-EZqZCXt4.ZKwZBIh6fivVYY9aqMzIi1x-jYFdyBAdmFuShHSXTZwnj4zPwsIwDuWIj.awKnaynwmvY3IopS9gtYUHvuo5c4UwktaVdPe4fl-T8T8CNJyGwPt8jYp86N75ZWGgSVe8AB94-10kAGkifk.jGhID2eRyL32yWx88Gg5sMVEit5Li1a9omSnYD7k82uOchREaTgIeqls.O.yOkHMs9XL7X7F27dOgw5eDYPoJzVo2zfFF2gvNE9IOU3TMH0uOLolAHzXsiE-V3nbGaFUdNW7MmgmYmADSxBtO3vyUBL6rdfVsMlRwLH.IvkbnOWL9FLmdwsve2bSlp6EGtEznML1qOg3RQjwqMcCL21Q8cVlzIUr0Q40zJTw7mrHU7ouhpB-w6QKYr6-obCy8oMbDMnKGJjIzEo7RDX1Te64pmIyTUs71RqHuOEszE0cjP8ekaQ6ARJJHQLN2BIgyVLWN5Dwur4uIujke4APsHniMp94bHiMvBF3QYMaThImqlXVTRoaFAwHRFES-F3FUF4hLk9t',
    'x-tt-passport-csrf-token': '9d53769d80f567f59f26026d80a350d7',
    'x-tt-passport-ttwid-ticket': 'AZ0p6iOR1d9L_o1W_4woEqeJzmI1Q-3AaFzrtQag65wZP7AZasxC5VngYKX_xRwalQ==',
}


email = input("email: ")


encoded_email = xor(email)


data_send = {
    'mix_mode': '1',
    'email': encoded_email,
    'type': '31',
    'aid': '1459',
    'is_sso': 'false',
    'account_sdk_source': 'web',
    'region': 'TR',
    'language': 'tr',
    'locale': 'tr-TR',
    'did': '7572540879727166983',
    'email_logic_type': '2',
    'fixed_mix_mode': '1',
}


url_send = 'https://login-no1a.www.tiktok.com/passport/web/email/send_code/?multi_login=1&did=7572540879727166983&locale=tr-TR&app_language=tr&aid=1459&account_sdk_source=web&sdk_version=2.1.11-tiktokbeta.3&language=tr&verifyFp=verify_mjiqefn2_MhPVrcLn_vbvN_4QbO_BZwh_xL997annY2Qu&target_aid=&standalone_aid=&shark_extra=%7B%22aid%22:1459,%22app_name%22:%22Tik_Tok_Login%22,%22channel%22:%22tiktok_web%22,%22device_platform%22:%22web_pc%22,%22device_id%22:%227572540879727166983%22,%22region%22:%22TR%22,%22priority_region%22:%22%22,%22os%22:%22windows%22,%22referer%22:%22https:%2F%2Fwww.tiktok.com%2Ftiktokstudio%2Fsound-library%3Ffrom%3Dcreator_center%22,%22root_referer%22:%22https:%2F%2Fwww.tiktok.com%2Ftiktokstudio%2Fsound-library%3Ffrom%3Dcreator_center%22,%22cookie_enabled%22:true,%22screen_width%22:1920,%22screen_height%22:1080,%22browser_language%22:%22tr-TR%22,%22browser_platform%22:%22Win32%22,%22browser_name%22:%22Mozilla%22,%22browser_version%22:%225.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F143.0.0.0+Safari%2F537.36%22,%22browser_online%22:true,%22verifyFp%22:%22verify_mjiqefn2_MhPVrcLn_vbvN_4QbO_BZwh_xL997annY2Qu%22,%22app_language%22:%22tr-TR%22,%22webcast_language%22:%22tr-TR%22,%22tz_name%22:%22Europe%2FIstanbul%22,%22is_page_visible%22:true,%22focus_state%22:true,%22is_fullscreen%22:false,%22history_len%22:9,%22user_is_login%22:false,%22data_collection_enabled%22:true%7D&msToken=rA83Eb2XH7CDj_vBOCqzOQ5jG8FGoomtsxFagGQCpjlAsB_S6d96uratTlhQ-A6GlwkCIjGYUwuO6Guwlc3sgxEBVSGS_BpnyfLTAIZdcy-vyGZYwmoiVU_X8Sw47yabhmNYwz9h1I3jmFM=&X-Bogus=DFSzsIVL4IDYhEmBCFGj8526xkVY&X-Gnarly=MKjm0MZs/9fOT2/fdOPE0aQxKK8suooH2ashQdaAxI4LKBB-oXvgq7C/JuYP28DseS4R5OsiAL1k0A5N3XXD9Wi7UnlNnxCsYF82TeZdw8M4DNzm39w803jXw8ip2hOFZpXLazNn4Fxl20bpcSAmjMCKWR0nvvhlegan8VuN1K/p/nTae3iMYZf24w9Rbs9nkU1y7OetTdUuXGC015RZIuFq1BO0ShZUjQkxeghT8NGnYV7OBRtVlRIYTe1FplVtBIfKjxSQXeymYr9U5sBCpuyRQv5RFRPTpj9aPy//Y/M7E0dTezyZ8le6OG6m/2IPx2R='
response_send = requests.post(url_send, cookies=cookies, headers=headers_send, data=data_send)

print("Send code response:", response_send.text)


code = input("cod: ")
new_password = input("new password: ")


encoded_code = xor(code)
encoded_new_password = xor(new_password)
encoded_email = xor(email)  


headers_options = {
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'tt-ticket-guard-client-data,tt-ticket-guard-iteration-version,tt-ticket-guard-public-key,tt-ticket-guard-version,tt-ticket-guard-web-version,x-mssdk-info,x-tt-passport-csrf-token,x-tt-passport-ttwid-ticket',
    'access-control-request-method': 'GET',
    'origin': 'https://www.tiktok.com',
    'priority': 'u=1, i',
    'referer': 'https://www.tiktok.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
}


reset_url = f'https://login-no1a.www.tiktok.com/passport/web/email/password/reset_and_login/?mix_mode=1&password={encoded_new_password}&email={encoded_email}&code={encoded_code}&aid=1459&is_sso=false&account_sdk_source=web&region=TR&language=tr&locale=tr-TR&did=7572540879727166983&rules_version=v2&fixed_mix_mode=1&multi_login=1&app_language=tr&sdk_version=2.1.11-tiktokbeta.3&verifyFp=verify_mjiqefn2_MhPVrcLn_vbvN_4QbO_BZwh_xL997annY2Qu&target_aid=&standalone_aid=&shark_extra=%7B%22aid%22:1459,%22app_name%22:%22Tik_Tok_Login%22,%22channel%22:%22tiktok_web%22,%22device_platform%22:%22web_pc%22,%22device_id%22:%227572540879727166983%22,%22region%22:%22TR%22,%22priority_region%22:%22%22,%22os%22:%22windows%22,%22referer%22:%22https:%2F%2Fwww.tiktok.com%2Ftiktokstudio%2Fsound-library%3Ffrom%3Dcreator_center%22,%22root_referer%22:%22https:%2F%2Fwww.tiktok.com%2Ftiktokstudio%2Fsound-library%3Ffrom%3Dcreator_center%22,%22cookie_enabled%22:true,%22screen_width%22:1920,%22screen_height%22:1080,%22browser_language%22:%22tr-TR%22,%22browser_platform%22:%22Win32%22,%22browser_name%22:%22Mozilla%22,%22browser_version%22:%225.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F143.0.0.0+Safari%2F537.36%22,%22browser_online%22:true,%22verifyFp%22:%22verify_mjiqefn2_MhPVrcLn_vbvN_4QbO_BZwh_xL997annY2Qu%22,%22app_language%22:%22tr-TR%22,%22webcast_language%22:%22tr-TR%22,%22tz_name%22:%22Europe%2FIstanbul%22,%22is_page_visible%22:true,%22focus_state%22:true,%22is_fullscreen%22:false,%22history_len%22:9,%22user_is_login%22:false,%22data_collection_enabled%22:true%7D&msToken=M110ThHiAE-G7evf3Pu3aEH1J22T-Yq9MingpOKmdGMMECK0tii9R81NpsmzZ401LwUCTtxkJoOPEtTfXWcNnoFwt2P7YbimMbVXwzvtUbJKECkCmqOmUWOCWuRYleCN48RdvbTJETVBtCA=&X-Bogus=DFSzsIVLSgAzVjmBCFGJfQ26xkao&X-Gnarly=MPGd74/rrdg0fMSshxhdyWNxPyWaZLQWI/yOO5PIPUiZ-x2MuEk-k57LCCOe/l7dqNN5r4qOoLDikc3x2qYHTwPOCirSA81jvfhKDzQoJqbXW3A8LeS-3amOgSQb8TmyX7KYkqByn7GGPrmwOH4N7QLfgQsRwbZ2-ZYMVkPvrOw4n4V44rQ3LmW49fJhAJDN6Pqa0rNplmH4gRLH0HmoHTX6aLUmwRq63YzAxbmb9-xq150JtEui5efWqePZvczJ3ipcjcPEQnNp66783WgjWtdfk75zPcRR9/skTtegOc9rRP9/i0FkXJZCxhLb-7zEzsI='


response_options = requests.options(reset_url, headers=headers_options)


headers_reset = headers_send.copy()  
headers_reset['accept'] = '*/*'
headers_reset.pop('content-type', None)  #eizon


response_reset = requests.get(reset_url, cookies=cookies, headers=headers_reset)

print("Reset response:", response_reset.text)


if response_reset.status_code == 200:
    print("password reset done.")
    username = input("username: ") 
    print(f"username: {username}")
    print(f"pass: {new_password}")
    print(f"email: {email}")
else:
    print("Reset failed.")




    # by @besteizon / @eizonxtool