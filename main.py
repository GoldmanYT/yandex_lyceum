import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name) as f:
            data = f.read()
    except Exception as e:
        return e

    res = ['']
    for i in data:
        if i == '\n':
            if len(res) == frame_height:
                break
            else:
                res.append('')
        else:
            if len(res[-1]) < frame_width:
                res[-1] += i
            else:
                if len(res) == frame_height:
                    break
                else:
                    res.append(i)

    return '\n'.join(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', type=int)
    parser.add_argument('--frame-width', type=int)
    parser.add_argument('file_name', type=str)
    args = parser.parse_args()
    print(format_text_block(args.frame_height, args.frame_width, args.file_name))
