# Main file running the converter to generate TSV data dumps from Exmaralda exb files
__author__ = 'zweiss'

from exmaralda_converter import generalhelper
import sys
import os

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Call\n> python main_converter.py INDIR OUTDIR")
        sys.exit(0)

    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    in_file_ending = ".exb"
    out_file_ending = ".tsv"

    file_list = generalhelper.GeneralHelper.rec_read_files(in_dir, file_ending=in_file_ending)

    for f in file_list:
        f_content = generalhelper.TSVDump.generate_cold_data_dump(in_file=f)
        # save the output
        out_file = f[f.rfind(os.path.sep)+1:f.rfind(in_file_ending)] + out_file_ending
        with open(os.path.join(out_dir, out_file), 'w', encoding="UTF-8") as outstr:
            outstr.write(f_content)

