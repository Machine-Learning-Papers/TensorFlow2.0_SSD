from xml.dom.minidom import parse
from configuration import PASCAL_VOC_DIR, OBJECT_CLASSES
import os

# parse one xml file
def parse_xml(xml):
    obj_and_box_list = []
    DOMTree = parse(xml)
    annotation = DOMTree.documentElement
    image_name = annotation.getElementsByTagName("filename")[0].childNodes[0].data

    obj = annotation.getElementsByTagName("object")
    for o in obj:
        o_list = []
        obj_name = o.getElementsByTagName("name")[0].childNodes[0].data
        o_list.append(OBJECT_CLASSES[obj_name])
        bndbox = o.getElementsByTagName("bndbox")
        for box in bndbox:
            xmin = box.getElementsByTagName("xmin")[0].childNodes[0].data
            ymin = box.getElementsByTagName("ymin")[0].childNodes[0].data
            xmax = box.getElementsByTagName("xmax")[0].childNodes[0].data
            ymax = box.getElementsByTagName("ymax")[0].childNodes[0].data
            o_list.append(xmin)
            o_list.append(ymin)
            o_list.append(xmax)
            o_list.append(ymax)
            break
        obj_and_box_list.append(o_list)
    return image_name, obj_and_box_list


if __name__ == '__main__':
    all_xml_dir = PASCAL_VOC_DIR + "Annotations"
    for item in os.listdir(all_xml_dir):
        item_dir = os.path.join(all_xml_dir, item)
        image_name, boxes_list = parse_xml(xml=item_dir)
        # print(image_name)
        # print(boxes_list)