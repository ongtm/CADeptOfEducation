import time


class DISTRICT:

    def __init__(
            self, cdcode, county, district, street, city, zipcode,
            state, mailstreet, mailcity, mailzip, mailstate, phone, extphone,
            faxnumber, email, admfname, admlname, admemail, lat, long,
            distrownercode, doctype, statustype, lastupdate):

        self.cdcode = cdcode
        self.county = county
        self.district = district
        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.state = state
        self.mailstreet = mailstreet
        self.mailcity = mailcity
        self.mailzip = mailzip
        self.mailstate = mailstate
        self.phone = phone
        self.extphone = extphone
        self.faxnumber = faxnumber
        self.email = email
        self.admfname = admfname
        self.admlname = admlname
        self.admemail = admemail
        self.lat = lat
        self.long = long
        self.distrownercode = distrownercode
        self.doctype = doctype
        self.statustype = statustype
        self.lastupdate = lastupdate

    def get_district_name(self):
        print(self.district)

    def get_district_cdcode(self):
        print(self.cdcode)

    def get_district_statustype(self):
        print(self.statustype)

def start_end_timer():
    print(time.perf_counter())


def read_text_file(strfile):
    f = open(strfile, "r")
    f.read()


def print_text_file(strfile):
    f = open(strfile, "r")
    print(f.read(3))


def load_text_file_to_class(strfile):
    t = open("/home/student/Desktop/schooldata/copiedfile.txt", "w")
    f = open(strfile, "r")
    next(f)


    for line in f:
        d = []
        d = line.split("\t")
        # print(d)
        # t.write(d)
        district = DISTRICT(d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9], d[10], d[11],
                            d[12], d[13], d[14], d[15], d[16], d[17], d[18], d[19], d[20], d[21], d[22], d[23])
        district.get_district_name()
        district.get_district_cdcode()
        district.get_district_statustype()

    f.close()
    t.close()


start_end_timer()
strfile = "/home/student/Desktop/schooldata/pubdistricts.txt"
load_text_file_to_class(strfile)
start_end_timer()

