import os
import csv
import json
# from PIL import Image, ImageDraw, ImageFont


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def to_csv(data, output_path):
    create_folder_if_not_exists(os.path.dirname(output_path))
    with open(output_path, 'w', newline='') as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"Printed out: {output_path}")


def to_json(data, output_path):
    create_folder_if_not_exists(os.path.dirname(output_path))
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Printed out: {output_path}")


def to_img(csv_input_name, output_path):
    create_folder_if_not_exists(os.path.dirname(output_path))
    data = []
    with open(csv_input_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)

    col_width_no = 60
    col_width = 180
    row_height = 50

    image_width = col_width * (len(data[0]) - 1) + col_width_no
    image_height = row_height * (len(data) + 1)

    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    for i, header in enumerate(data[0]):
        if i == 0:
            draw.rectangle([i * col_width_no, 0, (i + 1) *
                           col_width_no, row_height], fill="lightblue")
            draw.text((i * col_width_no + 10, 10),
                      header, font=font, fill="black")
        else:
            draw.rectangle([col_width_no + (i - 1) * col_width, 0,
                           col_width_no + i * col_width, row_height], fill="lightblue")
            draw.text((col_width_no + (i - 1) * col_width + 10, 10),
                      header, font=font, fill="black")

    for i, row in enumerate(data[1:], start=1):
        for j, value in enumerate(row):
            if j == 0:
                draw.rectangle([j * col_width_no, i * row_height, (j + 1)
                               * col_width_no, (i + 1) * row_height], fill="white")
                draw.text((j * col_width_no + 10, i * row_height + 10),
                          value, font=font, fill="black")
            else:
                draw.rectangle([col_width_no + (j - 1) * col_width, i * row_height,
                               col_width_no + j * col_width, (i + 1) * row_height], fill="white")
                draw.text((col_width_no + (j - 1) * col_width + 10,
                          i * row_height + 10), value, font=font, fill="black")

    image.save(output_path)
    print(f"Printed out: {output_path}")
