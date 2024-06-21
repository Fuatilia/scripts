import os
import json
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import process

name_list = """
1. Hon. Samuel Chepkonga - YES
2. Hon. Benjamin Kipkirui - YES
3. Hon. Marianne Kitany - YES
4. Hon. Samuel Atandi - NO
5. Hon. John Walter Owino - NO
6. Hon. Irene Njoki - ABSENT
7. Hon. Abdi Shurie - ABSENT
8. Hon. Florence Jematia - YES
9. Hon. Joshua Kandie - YES
10. Hon. Kipkoros Makilap - YES
11. Hon. Charles Kamuren - YES
12. Hon. Koech Nelson - YES
13. Hon. Barongo Nolphason - NO
14. Hon. Alpha Miruka - YES
15. Hon. Linet Chepkorir - YES
16. Hon. Richard Cheruiyot - YES
17. Hon. Yegon Richard - YES
18. Hon. Gideon Ochanda - YES
19. Hon. Osero Patrick Kibagendi - NO
20. Hon. Raphael Wanjala - NO
21. Hon. Jack Wamboka - NO
22. Hon. Catherine Wambilianga - YES
23. Hon. Yakub Adow - ABSENT
24. Hon. Komingoi Kibet - YES
24. Hon. Catherine Omanyo - NO
25. Hon. Tindi Mwale - NO
26. Hon. Oyula Joseph - NO
27. Hon. Rindikiri Mugambi - YES
28. Hon. Kirima Nguchine - YES
29. Hon. Omar Shimbwa Mwinyi - NO
30. Hon. Victor Koech - YES
31. Hon. Patrick Simiyu - NO
32. Hon. Byego Paul Kibichii - YES
33. Hon. Patrick Ntwiga - YES
34. Hon. Farah Maalim - YES
35. Hon. Beatrice Elachi - NO '
36. Hon. John Kiarie - YES
37. Hon. Musa Sirma - YES
38. Hon Adan Keynan - YES
39. Hon. Jeptoo Caroline Ngelechei - YES
40. Hon. Mejjadonk Benjamin - ABSENT
41. Hon. Babu Owino - NO
42. Hon. James Gakuya - ABSENT
43. Hon. Julius Mawathe - NO
44. Hon. Mark Mwenje - NO
45. Hon. Lelemengit Josses - YES
46. Hon. Omboko Milemba - YES
47. Hon. Johana Ngeno - YES
48. Hon. Robert Pukose - YES
49. Hon. Yakub Farah - YES
50. Hon. Oundo Ojiambo - NO
51. Hon. Hiribae Said - ABSENT
52. Hon. Tungule Charo Kazungu - YES
53. Hon. Udgoon Siyyad - NO
54. Hon. Baro Dekow - YES
55. Hon. Guyo Ali Wario - YES
56. Hon. Edward Wakili - YES
57. Hon. Kururia Njoroge - YES
58. Hon. Gabriel Kagombe - YES
59. Hon. Elisha Odhiambo - NO
60. Hon. Robert Gichimu - YES
61. Hon. Martha Wangari - YES
62. Hon. Gathoni Wamuchomba - NO
63. Hon. Gimose Gumini - YES
64. Hon. Joyce Bensuda - NO
65. Hon. George Kaluma - NO
66. Hon. Karithi Kiili - YES
67. Hon. Julius Taitumu - YES
68. Hon. John Paul Mwirigi - YES
69. Hon. Ali Abdi Ali - YES
70. Hon. Bernard Shinali - YES
71. Hon. Mumina Bonaya - YES
72. Hon. Lomwaa Joseph Samal - ABSENT
73. Hon. Tubi Mohamed - (UNWELL and communicated with Speaker)
74. Hon. Bady Bady Twalib - NO
75. Hon. George Koimburi - NO
76. Hon. Wamacukuru James - YES
77. Hon Eve Obara - NO
78. Hon.  Kalasinga Majimbo - NO
79. Hon. Titus Lotee - YES
80. Hon. Joseph Kimilu - NO
81. Hon Leah Sankaire - YES
82. Hon. Memusi Kanchory - YES
83. Hon. Kakuta Maimai - NO
84. Hon. Onesmus Ngogoyo - YES
85. Hon. Sakimba Parashina - NO
86. Hon. Sunkuiya George - YES
87. Hon. Elsie Muhanda - NO
88. Hon. Paul Katana - NO
89. Hon. Yussuf Hassan - NO
90. Hon. Chege Njuguna - YES
91. Hon. John Makali - YES
92. Hon. Peter Irungu - YES
93. Hon Fabian Kyule - YES
94. Hon. Moroto Samuel - YES
95. Hon. Oscar Sudi - YES
96. Hon. Adipo Okuome - NO
97. Hon. Ronald Karauri - YES
98. Hon. Charles Were - NO
99. Hon. Robert Mbui - NO
100. Hon. Adams Kipsanai - YES
101. Hon. Gideon Kimaiyo - YES
102. Hon. Beatrice Kemei - YES
103. Hon. Julius Ruto - YES
104. Hon. Christopher Aseka - YES
105. Hon. John Kawanjiku - YES
106. Hon. Waithaka John - YES
107. Hon Wamuratha Wanjiku - YES
108. Hon. Peter Orero - NO
109. Hon. Jessica Mbalu - NO
110. Hon Mwengi Mutuse - YES
111. Hon. Njoroge Wainaina - YES
112. Hon. Joseph Munyoro - YES
114. Hon. Ndindi Nyoro - YES
115. Hon. Kimani Ichung'wah - YES
116. Hon. Julius Sunkuli - NO
117. Hon. Gertrude Mbeyu - NO
118. Hon. Owen Baya - YES
119. Hon. Ken Chonga - NO
120. Hon Nzambia Kithua - NO
121. Hon. Didmus Barasa - YES
122. Hon. Kakai Bisau - NO
123. Hon. Gonzi Rai - YES
124. Hon. Kwenya Thuku - YES
125. Hon. Wanjiku Muhia - YES
126. Hon. Cherorot Joseph - YES
127. Hon. Hillary Kosgei - YES
128. Hon. Jane Maina Njeri - ABSENT
129. Hon. Joseph Gitari - YES
130. Hon. Bedzimba Rashid - NO
131. Hon. Donya Doris - ABSENT
132. Hon. Ruth Odinga - NO
133. Hon. Oron Joshua - NO
134. Hon. Shakeel Shabbir - ABSENT
135. Hon. Rozaah Buyu - NO
136. Hon. Irene Kasalu - NO
137. Hon. Makali Mulu - NO
138. Hon. Nimrod Mbai - YES
139. Hon. Mboni Mwalika - NO
140. Hon. Rachael Nyamai - YES
141. Hon. Edith Nyenze - NO
142. Hon. Japheth Nyakundi - YES
143. Hon. Kibagendi Anthony - NO
144. Hon. Clive Gisairo - NO
145. Hon. Yegon Richard - YES
146. Hon. Alfred Mutai - YES
147. Hon. Joseph Tonui - YES
148. Hon. Kitayama Maisori - YES
149. Hon. Mathias Robi - YES
150. Hon. Fatuma Masito - NO
151. Hon Ferdinand Wanyonyi - YES
152. Hon. Abdulrahman Mohamed - NO
153. Hon Mohamed Hussein Abdekadir - YES
154. Hon. Jane Kagiri - YES
155. Hon. Mwangi Kiunjuri - YES
156. Hon. Sarah Korere - YES
157. Hon. Stephen Wachira Karani - YES
158. Hon. Joseph Lekuton - YES
159. Hon. Muthoni Marubu - YES
160. Hon. Ruweida Obo - YES
161. Hon. Stanley Muthama - YES
162. Hon. Phelix Odiwuor (Jalang'o) - NO
163. Hon. Kahangara Joseph - YES
164. Hon. Mishi Mboko - NO
165. Hon. Innocent Mugabe - NO
166. Hon. John Chege Kiragu - YES
167. Hon. Protus Akuja - YES
168. Hon. Dick Maungu - NO
169. Hon, Nabii Nabwera - NO
170. Hon. Chiforomodo Mangale - YES
171. Hon. Titus Khamala - NO
172. Hon. Kareke Mbiuki - YES
173. Hon. Joyce Kamene - NO
174. Hon. Caleb Mule - YES
175. Hon. George Aladwa - NO
176. Hon. Suzanne Kiamba - NO
177. Hon. Rose Mumo - NO
178. Hon. Malulu Injendi - YES
179. Hon. Amina Mnyazi - NO
180. Hon. Sheikh Bashir Abdullahi - YES
181. Hon. Umul kher Kassim - YES
182. Hon. Husseinweytan Mohamed - NO
183. Hon. Abdul Haro Ibrahim - YES
184. Hon. Yusuf Adan Haji - YES
185. Hon. John Mukunji - NO
186. Hon. Wamaua Njoroge - YES
187. Hon. David Bowen - YES
188. Hon.  Kipchumba Toroitich - YES
189. Hon. Naomi Waqo - YES
190. Hon. Joshua Mwaliyo - ABSENT
191. Hon. Geoffrey Odanga - NO
192. Hon. Anthony Oluoch - NO
193. Hon. Eric Mwangi Kahugu - YES
194. Hon. Kassim Sawa - YES
195. Hon. Peter OScar Nabulindo - YES
196. Hon. Stephen Mule - NO
197. Hon. Geoffrey Kariuki - YES
198. Hon. Bernard Muriuki - YES
199. Hon. Erastus Kivasu - NO
200. Hon. Elizabeth Kailemia - YES
201. Hon. Fatuma Zainab - NO
202. Hon. Kiborek Reuben - YES
203. Hon. Bartoo Phyllis - YES
204. Hon. Kuria Kimani - YES
205. Hon. Zamzam Mohamed - NO
206. Hon. Abraham Kirwa - YES
207. Hon. Feisal Bader - YES
208. Hon. Fred Kapondi - YES
209. Hon. K'oyoo James - NO
210. Hon. Kaguchia John - YES
211. Hon. Salasya Peter - NO
212. Hon. Johnson Naicca - YES
213. Hon. Betty Maina - YES
214. Hon. Machele Mohamed - NO
215. Hon. Musyoka Vincent - YES
216. Hon. Mary Maingi - YES
217. Hon. Gideon Mulyungi - NO
218. Hon. Paul Nzengu - NO
219. Hon. Charles Nguna - NO
220. Hon. Esther Passaris - NO
221. Hon. Jayne Kihara - YES
222. Hon. Liza Chelule - YES
223. Hon. David Gikaria - YES
224. Hon. Samuel Arama - YES
225. Hon. Godfrey Mulanya - NO
226. Hon. Cynthia Muge - YES
227. Hon. Bernard Kitur - ABSENT
228. Hon. Rebecca Tonkei - YES
229. Hon. Aramat Lemanken - YES
230. Hon. Gabriel Tongoyo - YES
231. Hon. Emmanuel Wangwe - YES
232. Hon. George Gachagua - YES
233. Hon. Martin Peters Owino - NO
233. Hon. GK Kariuki - YES
234. Hon. Charity Kathambi - YES
235. Hon. Guyo Adhe - YES
236. Hon. Rahim Dawood - YES
237. Hon Joash Nyamoko - YES
238. Hon. Aduma Owuor - NO
239. Hon. Mohamed Ali - ABSENT
240. Hon. Jerusha Momanyi - YES
241. Hon. Faith Gitau - YES
242. Hon Jared Okelo - NO
243. Hon. Zaheer Jhanda - YES
244. Hon. Daniel Manduku - NO
245. Hon. Tom Mboya Odege - NO
246. Hon. Rahab Mukami - YES
247. Hon. Duncan Mathenge - YES
248. Hon. Michael Muchira - YES
249. Hon. Kiaraho David - YES
250. Hon. Michael Wainaina - YES
251. Hon. David Pkosing - YES
252. Hon. Antony Kenga - NO
253. Hon. Lilian Gogo - NO
254. Hon. Otiende Amolo - NO
255. Hon. Kibet Jebor - YES
256. Hon. Paul Abuor - NO
257. Hon. Mwafrika Kamande - YES
258. Hon. TJ Kajwang - NO
259. Hon. Simon Kingara - YES
260. Hon. Eric Karemba - YES
261. Hon. Sloya Clement - ABSENT
262. Hon. Caleb Amisi - NO
263. Hon. Dido Rasso - YES
264. Hon. Pauline Lenguris - YES
265. Hon. Lekumontare Jackson - YES
266. Hon. Letipila Dominic - YES
267. Hon. Naisula Lesuuda - NO
268. Hon. James Nyikal - NO
269. Hon. Fredrick Ikana - YES
270. Hon. Christine Ombaka - NO
271. Hon. Peter Lochakapong - YES
272. Hon. Justice Kemei - YES
273. Hon. John WalkWaluke - YES
274. Hon. Francis Sigei - YES
275. Hon. Shadrack Mwiti - ABSENT
276. Hon. Silvanus Osoro - YES
277. Hon. David Kiplagat - YES
278. Hon. Amos Mwago - NO
279. Hon. Millie Odhiambo - NO
280. Hon. Caroli Omondi - YES
281. Hon. Samuel Gachobe - YES
282. Hon. Junet Mohamed - NO
283. Hon. Francis Masara - NO
284. Hon. Amina Dika - YES
285. Hon. Bare Hussein Abdi - YES
286. Hon. John Bwire - YES
287. Hon. Oku Kaunya - NO
288. Hon. Mary Emaase - YES
289. Hon. Geoffrey Wandeto - ABSENT
290. Hon. George Murugara - YES
291. Hon. Susan Ngugi - ABSENT
292. Hon. Alice Ng'ang'a - YES
293. Hon. William Kamket - YES
294. Hon. Mpuru Aburi - YES
295. Hon. John Mutunga - YES
296. Hon. Julius Melly - YES
297. Hon John Chikati - YES
298. Hon. Lilian Siyoi - YES
299. Hon. Janet Sitienei - YES
300. Hon. Cecilia Ngitit - ABSENT
301. Hon. Joseph Namuar - YES
302. Hon. Paul Ekuom Nabuin - NO
303. Hon John Ariko - NO
304. Hon. Daniel Nanok - YES
305. Hon. Gladys Shollei - YES
306. Hon. David Ochieng - NO
307. Hon. James Wandayi - NO
308. Hon. Mark Nyamita - NO
309. Hon Ernest Kivai Kagesi - YES
310. Hon. Beatrice Adagala - YES
311. Hon. Adow Mohamed - YES
312. Hon. Farah Yusuf Mohamed - NO
313. Hon. Martin Pepela - YES
314. Hon. Abdi Daudi Mohamed - ABSENT
315. Hon. Daniel Wanyama - YES
316. Hon. Stephen Mogaka - NO
317. Hon. Rael Chepkemoi - YES
318. Hon. Timothy Wanyonyi - NO
319. Hon. Mwakuwona Danson - NO
320. Hon. Basil Robert - NO
321. Hon. Abdisirat Khalif - YES
322. Hon. Sabina Chege - ABSENT
323. Hon. Joseph Hamisi - YES
324. Hon. Harun Suleka - YES
325. Hon. Ikiara Dorothy - YES
326. Hon. Iraya Joseph - YES
327. Hon. Kosgei Joseph - ABSENT
328. Hon. Irene Mayaka - NO
329. Hon. Umul kher Harun - NO
330. Hon. Teresia Wanjiru Mwangi -  ABSENT
331. Hon. John Mbadi - NO
332. Hon. Talib Abubakar Ahmed - YES
333. Hon. Harrison Garama - ABSENT
334. Hon. Gichuki Edwin Mugo - YES
335. Hon. Jackson Kipkemoi Kosgei - YES
"""

provided_dict = {}
for line in name_list.strip().split("\n"):
    name, vote = line.rsplit(" - ", 1)
    name_without_number = name.split(". ", 1)[1]
    provided_dict[name_without_number] = vote.strip()

print(provided_dict)

base_url = "http://www.parliament.go.ke/the-national-assembly/mps"
params = {"field_name_value": "", "field_parliament_value": "2022", "field_employment_history_value": ""}
current_page = 0

mp_list = []

while True:
    params["page"] = current_page

    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")

    if table is None:
        break


    rows = table.find_all("tr")

    if len(rows) <= 1:
        break

    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 6:
            name = cells[0].text.strip()
            county = cells[2].text.strip()
            constituency = cells[3].text.strip()
            party = cells[4].text.strip()
            status = cells[5].text.strip()

            img_tag = cells[1].find('img')
            img_src = img_tag['src'] if img_tag else 'N/A'

            if img_src != 'N/A':
                img_url = f"http://www.parliament.go.ke{img_src}"

                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    img_filename = f"{name.replace(' ', '_')}.jpg"
                    img_path = os.path.join('mp_images', img_filename)
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_response.content)

            mp_list.append({
                "name": name,
                "county": county,
                "constituency": constituency,
                "party": party,
                "status": status,
                "img_src": img_src,
                "img_path": img_path
            })

            print(f"Name: {name}, Constituency: {constituency}")

    current_page += 1

mp_names = [mp['name'] for mp in mp_list]
for name, vote in provided_dict.items():
    match, score = process.extractOne(name, mp_names)
    print(name, match,  score)
    if score > 80:
        for mp in mp_list:
            if mp['name'] == match:
                mp['financeBillVote'] = vote
                break

output_data = {
    "count": len(mp_list),
    "mps": mp_list
}

with open('mp_data.json', 'w') as json_file:
    json.dump(output_data, json_file, indent=4)

print(f"Total MPs: {output_data['count']}")