from django.shortcuts import render
from PIL import Image
from django.http import HttpResponse


def Blue_shoes(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    if 255 >= r >= 100 and 255 >= g >= 100 and 255 >= b >= 100:
        result = [int(r - 255), int(b - 0), int(g - 0)]
    else:
        result = [r, g, b]
    return tuple(result)


def Magenta_shoes(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    if 255 >= r >= 100 and 255 >= g >= 100 and 255 >= b >= 100:
        result = [int(r - 0), int(b - 255), int(g - 0)]
    else:
        result = [r, g, b]
    return tuple(result)


def Yellow_shoes(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    if 255 >= r >= 100 and 255 >= g >= 100 and 255 >= b >= 100:
        result = [int(r - 0), int(b - 0), int(g - 255)]
    else:
        result = [r, g, b]
    return tuple(result)


def apply_filter(img: Image.Image, filt) -> Image.Image:
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))
            new_pixel = filt(r, g, b)
            img.putpixel((i, j), new_pixel)
    return img


def process_img(request):
    filter_names = [
        "Покрасить в голубой",
        "Покрасить в пурпурный",
        "Покрасить в желтый",
    ]

    filters = [
        Blue_shoes,
        Magenta_shoes,
        Yellow_shoes,
    ]
    if request.method == "POST":
        is_finished = False

        while not is_finished:
            img_file = request.FILES["image"]
            image = Image.open(img_file)

            # image.show()
            print("В какой цвет покрасить кеды? >>> ?")

            for i in range(len(filter_names)):
                print(f"{i} - {filter_names[i]}")

            choice = input("Выберите фильтр (введите номер): >>> ")

            while not choice.isdigit() or int(choice) >= len(filters):
                choice = input("Некорректный ввод. Попробуйте еще раз >>> ")

            filt = filters[int(choice)]
            image = apply_filter(image, filt)

            image.show()
            answer = input("Еще раз? (да/нет): ")

            while answer != "да" and answer != "нет":
                answer = input("Некорректный ввод. Попробуйте еще раз >>> ")

            if answer == "нет":
                end = False
                while not end:
                    save_file = input("Сохранить изменения? (да/нет): ")

                    while save_file != "да" and save_file != "нет":
                        save_file = input("Некорректный ввод. Попробуйте еще раз >>> ")

                    if save_file == "нет":
                        end = save_file == "нет"

                    if save_file == "да":
                        image.save("appname/static/image/newIMGG.jpeg")
                        end = save_file == "да"

            is_finished = answer == "нет"

    return render(request, "upload_img.html")
