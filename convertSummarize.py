import json
from datetime import datetime

# Sample JSON data
data = {
    "timeline": [
        {
            "day": "2024-11-05",
            "events": [
                {
                    "time": "2024-11-05T09:00:00",
                    "name": "Khởi hành từ Hà Nội",
                    "place": ""
                },
                {
                    "time": "2024-11-05T12:30:00",
                    "name": "Đến Đà Nẵng",
                    "place": ""
                },
                {
                    "time": "2024-11-05T14:00:00",
                    "name": "Tham quan bãi biển Mỹ Khê",
                    "place": "Bãi biển Mỹ Khê"
                },
                {
                    "time": "2024-11-05T18:00:00",
                    "name": "Ăn tối tại nhà hàng biển",
                    "place": "Nhà hàng Biển"
                }
            ]
        },
        {
            "day": "2024-11-06",
            "events": [
                {
                    "time": "2024-11-06T08:30:00",
                    "name": "Tham quan Phố cổ Hội An",
                    "place": "Hội An"
                },
                {
                    "time": "2024-11-06T13:00:00",
                    "name": "Ăn trưa tại Hội An",
                    "place": ""
                },
                {
                    "time": "2024-11-06T15:30:00",
                    "name": "Trải nghiệm làm gốm",
                    "place": "Làng gốm Thanh Hà"
                },
                {
                    "time": "2024-11-06T19:30:00",
                    "name": "Xem biểu diễn ánh sáng phố cổ",
                    "place": "Phố cổ Hội An"
                }
            ]
        },
        {
            "day": "2024-11-07",
            "events": [
                {
                    "time": "2024-11-07T09:00:00",
                    "name": "Khởi hành về Hà Nội",
                    "place": ""
                },
                {
                    "time": "2024-11-07T12:00:00",
                    "name": "Dừng chân nghỉ ngơi",
                    "place": "Nhà hàng trên đường"
                },
                {
                    "time": "2024-11-07T16:00:00",
                    "name": "Về đến Hà Nội",
                    "place": ""
                }
            ]
        }
    ]
}


def convert_timeline_to_sentences(timeline):
    sentences = []
    for day_entry in timeline:
        day = day_entry["day"]
        dayStr = datetime.fromisoformat(day).strftime("%d/%m/%Y")
        sentences.append(f"Ngày {(dayStr)} có lịch trình sau:")
        for event in day_entry["events"]:
            time = datetime.fromisoformat(event["time"])  
            formatted_time = time.strftime("%H:%M")  
            name = event["name"]
            place = event["place"]
            if place:
                sentences.append(f"- Lúc {formatted_time}, {name} tại {place}.")
            else:
                sentences.append(f"- Lúc {formatted_time}, {name}.")
    return sentences

timeline_sentences = convert_timeline_to_sentences(data["timeline"])
for sentence in timeline_sentences:
    print(sentence)