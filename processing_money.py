from collections import Counter

def iou(box1, box2):

    x1 = max(box1["x1"], box2["x1"])
    y1 = max(box1["y1"], box2["y1"])
    x2 = min(box1["x2"], box2["x2"])
    y2 = min(box1["y2"], box2["y2"])


    # площадь пересечения двух прямоугольников
    inter = max(0, x2-x1) * max(0, y2-y1)

    # площадь каждого прямоугльника детекта
    area1 = (box1["x2"]-box1["x1"]) * (box1["y2"]-box1["y1"])
    area2 = (box2["x2"]-box2["x1"]) * (box2["y2"]-box2["y1"])

    # площадь наложения двух прямоугольников
    union = area1 + area2 - inter

    # Если площадь наложения больше 0, то возвращаем отношение площади пересечения к площади объединения, иначе 0
    return inter / union if union > 0 else 0

def remove_duplicates(detections, iou_threshold=0.5):

    detections = sorted(detections, key=lambda x: x["confidence"], reverse=True)

    result = []

    while detections:

        #Берем самый уверенный детект
        best = detections.pop(0)
        result.append(best)

        #Убираем все детекты, которые сильно пересекаются с ним
        detections = [
            d for d in detections
            if iou(best["box"], d["box"]) < iou_threshold
        ]

    return result

def count_money(counts):
    
    total = 0
    
    values = {
        "coin_1": 1,
        "coin_2": 2,
        "coin_5": 5,
        "coin_10": 10,
        "bill_5": 5,
        "bill_10": 10,
        "bill_50": 50,
        "bill_100": 100,
        "bill_200": 200,
        "bill_500": 500,
        "bill_1000": 1000,
        "bill_2000": 2000,
        "bill_5000": 5000
    }
    
    for name, count in counts.items():
        value = values[name]
        subtotal = value * count
        total += subtotal
        
        print(f"{name}: {count} x {value} = {subtotal}")
    print(f"Total: {total}")