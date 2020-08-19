__author__ = 'zweiss'

import os
from exmaralda_converter import exmaralda


class TSVDump:

    @staticmethod
    def generate_cold_data_dump(in_file):

        # load the transcript
        cold_transcript = exmaralda.ExmaraldaTranscript.load(in_file)

        # create a data table
        rval = 'Tier-ID\tType\tDisplay Name\tCategory\tSpeaker-ID\tAbbreviation\tL1\tL2\tLanguages Used\tSex\tStart\tEnd\tString\n'
        for tid in cold_transcript.tiers:
            tier = cold_transcript.tiers[tid]
            typ = tier.type if len(tier.type) > 0 else 'NA'
            dname = tier.display_name if len(tier.display_name) > 0 else 'NA'
            cat = tier.category if len(tier.category) > 0 else 'NA'
            sid = "NA"
            abb = "NA"
            l1 = "NA"
            l2 = "NA"
            luse = "NA"
            sex = "NA"

            if len(tier.speaker) > 0 and tier.speaker in cold_transcript.speaker_table.keys():
                sid = tier.speaker
                abb = cold_transcript.speaker_table[sid].abbreviation if len(cold_transcript.speaker_table[sid].abbreviation) > 0 else 'NA'
                l1 = '_'.join(cold_transcript.speaker_table[sid].l1) if len(cold_transcript.speaker_table[sid].l1) > 0 else 'NA'
                l2 = '_'.join(cold_transcript.speaker_table[sid].l2) if len(cold_transcript.speaker_table[sid].l2) > 0 else 'NA'
                luse = '_'.join(cold_transcript.speaker_table[sid].languages_used) if len(cold_transcript.speaker_table[sid].languages_used) > 0 else 'NA'
                sex = cold_transcript.speaker_table[sid].sex if len(cold_transcript.speaker_table[sid].sex) > 0 else 'NA'

            prefix = tid + "\t" + typ + "\t" + dname + "\t" + cat + "\t" + sid + "\t" + abb + "\t" + l1 + "\t" + l2 + "\t" + luse + "\t" + sex + "\t"

            for e in tier.event_list:
                stime = cold_transcript.timeline[e.start.time_id].time_stamp
                etime = cold_transcript.timeline[e.end.time_id].time_stamp
                rval += prefix + stime + "\t" + etime + "\t" + e.content
                if cat == "v" and (e.content.endswith(".") or e.content.endswith("!") or e.content.endswith("?")):
                    #print(rval)
                    rval += " "
                rval += "\n"
        return rval


class GeneralHelper:

    @staticmethod
    def rec_read_files(in_dir, file_ending=".exb"):
        rval = []
        for root, dirs, files in os.walk(in_dir):
            for f in files:
                if f.startswith(".") or not f.endswith(file_ending):
                    continue
                rval.append(os.path.join(root,f))
        return rval
