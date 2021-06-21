from argparse import ArgumentParser
from pathlib import Path
import img2pdf

def main(input_pth, output_pth):
    inp, out = Path(input_pth).absolute(), Path(output_pth)
    ## Load Input Images
    if inp.is_dir():
        print(f"Input images folder : {input_pth}")
        imgs = sorted([str(image) for image in inp.glob('**/*.png')])
        print(f"Number of pages = {len(imgs)}")
    else:
        print(f"WARNING! Please check the input folder again.")
        return

    ## Check output folder
    out.mkdir(exist_ok=True)
    out_file = Path.joinpath(out, inp.stem +'.pdf')
    print('Start to convert, it may take some time.')
    with open(out_file, 'wb') as w:
        w.write(img2pdf.convert(imgs))
    print(f'\nDone !\nFind the file here : {out_file}\n')



if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-i", "--input", help="Input images' folder name", required=True)
    parser.add_argument("-o", "--output", help="Output folder", default='./pdfs')
    args = parser.parse_args()

    main(args.input, args.output)

