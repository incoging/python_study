# 这个文档用户合成gif图片
import imageio


def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.1)

    return


def main():
    image_list = ['test_gif-0.png', 'test_gif-2.png', 'test_gif-4.png',
                  'test_gif-6.png', 'test_gif-8.png', 'test_gif-10.png']
    gif_name = 'created_gif.gif'
    create_gif(image_list, gif_name)


if __name__ == "__main__":
    main()