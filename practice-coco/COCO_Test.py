{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPVYVZJkCKdDqTQV7grVcKW"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lt6D493eBF9J",
        "outputId": "adba4d39-9885-46ad-8e15-2987629b2c3f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: pycocotools in /usr/local/lib/python3.7/dist-packages (2.0.5)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from pycocotools) (1.21.6)\n",
            "Requirement already satisfied: matplotlib>=2.1.0 in /usr/local/lib/python3.7/dist-packages (from pycocotools) (3.2.2)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=2.1.0->pycocotools) (2.8.2)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=2.1.0->pycocotools) (1.4.4)\n",
            "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=2.1.0->pycocotools) (3.0.9)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=2.1.0->pycocotools) (0.11.0)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.7/dist-packages (from kiwisolver>=1.0.1->matplotlib>=2.1.0->pycocotools) (4.1.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.1->matplotlib>=2.1.0->pycocotools) (1.15.0)\n"
          ]
        }
      ],
      "source": [
        "import json\n",
        "from PIL import Image\n",
        "import matplotlib.pyplot as plt\n",
        "import matplotlib.patches as patches\n",
        "from PIL import Image\n",
        "\n",
        "# For using COCO API\n",
        "!pip install pycocotools\n",
        "from pycocotools.coco import COCO"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Downloading dataset\n",
        "# Ran out of disk space if I tried to add any other files\n",
        "!wget http://images.cocodataset.org/zips/train2017.zip\n",
        "\n",
        "!unzip train2017.zip"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jB5oJjX5B9kB",
        "outputId": "eae5c2db-ac0e-4d3e-f018-0166bc54ed4a"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2022-10-11 00:26:34--  http://images.cocodataset.org/zips/train2017.zip\n",
            "Resolving images.cocodataset.org (images.cocodataset.org)... 52.216.25.148\n",
            "Connecting to images.cocodataset.org (images.cocodataset.org)|52.216.25.148|:80... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 19336861798 (18G) [application/zip]\n",
            "Saving to: ‘train2017.zip.1’\n",
            "\n",
            "train2017.zip.1      47%[========>           ]   8.56G  74.7MB/s    eta 2m 10s ^C\n",
            "Archive:  train2017.zip\n",
            "replace train2017/000000147328.jpg? [y]es, [n]o, [A]ll, [N]one, [r]ename: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "coco = COCO(\"train2017\")\n",
        "\n",
        "# Get list of category_ids\n",
        "# Used bicycles in this to test\n",
        "category_ids = coco.getCatIds(['bicycle'])\n",
        "\n",
        "# Get list of image_ids which contain bicycles\n",
        "image_ids = coco.getImgIds(catIds=[2])\n",
        "print(image_ids[0:5])"
      ],
      "metadata": {
        "id": "s_P4C0IRKqHE",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 240
        },
        "outputId": "9dc536e4-ff77-4af7-f90a-2a9a3abc2abc"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-5-06c2aca63aeb>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mcoco\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mCOCO\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"train2017\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;31m# Get list of category_ids, here [2] for bicycle\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mcategory_ids\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcoco\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetCatIds\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'bicycle'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'COCO' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Getting annotation ids of random image from bicycle data\n",
        "annotation_ids = coco.getAnnIds(imgIds=196610, catIds=[2])\n",
        "print(len(annotation_ids))\n",
        "\n",
        "anns = coco.loadAnns(annotation_ids)\n",
        "\n",
        "# Getting annotation coords\n",
        "for ann in anns:\n",
        "    print(ann['bbox'])"
      ],
      "metadata": {
        "id": "Bxq-X08cYoY1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "image_id = 196610\n",
        " \n",
        "images_path = \"train2017\"\n",
        "image_name = str(image_id).zfill(12)+\".jpg\"\n",
        "image = Image.open(images_path+image_name) # Had issue here opening images by path+name\n",
        " \n",
        "fig, ax = plt.subplots()\n",
        " \n",
        "# Draw boxes and add label to each box\n",
        "for ann in anns:\n",
        "    box = ann['bbox']\n",
        "    bb = patches.Rectangle((box[0],box[1]), box[2],box[3], linewidth=2, edgecolor=\"blue\", facecolor=\"none\")\n",
        "    ax.add_patch(bb)\n",
        " \n",
        "ax.imshow(image)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 365
        },
        "id": "hldt2-JHdBAa",
        "outputId": "d563850f-b1df-4e47-fc22-66d49d6a3ded"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-9-9dadff42c642>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mimages_path\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"train2017\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mimage_name\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimage_id\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mzfill\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m12\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;34m\".jpg\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0mimage\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mImage\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimage_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0mfig\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0max\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msubplots\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/PIL/Image.py\u001b[0m in \u001b[0;36mopen\u001b[0;34m(fp, mode)\u001b[0m\n\u001b[1;32m   2841\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2842\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mfilename\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2843\u001b[0;31m         \u001b[0mfp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbuiltins\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"rb\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2844\u001b[0m         \u001b[0mexclusive_fp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2845\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '000000196610.jpg'"
          ]
        }
      ]
    }
  ]
}