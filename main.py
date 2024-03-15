from classes import AddressBook, NoteBook  # модуль з класами
import func  # модуль з функціями виконання команд боту
import features  # модуль з фічами


def main():
    '''
     Main function
    '''

    # ініціалізація
    book = AddressBook()
    notes = NoteBook()
    features.greeting()

    # work cycle
    while True:

        # parsing
        user_input = input("Enter a command >>> ")
        if user_input:
            command, args = func.parse_input(user_input)
        else:
            continue

        # handling
        if command in ("close", "exit", "quit"):
            features.goodbye()
            break

        elif command == "help":
            func.help_doc()

        elif command == "hello":
            func.hello()

        elif command == "add-man":
            func.add_man(args, book)
            func.save_book(book)

        elif command == "del-man":
            func.del_man(args, book)
            func.save_book(book)

        elif command == "cng-man":
            func.cng_man(args, book)
            func.save_book(book)

        elif command == "show-man":
            func.show_man(args, book)

        elif command == "find-man":
            func.find_man(args, book)

        elif command == "add-phone":
            func.add_phone(args, book)
            func.save_book(book)

        elif command == "cng-phone":
            func.cng_phone(args, book)
            func.save_book(book)

        elif command == "del-phone":
            func.del_phone(args, book)
            func.save_book(book)

        elif command == "add-email":
            func.add_email(args, book)
            func.save_book(book)

        elif command == "cng-email":
            func.cng_email(args, book)
            func.save_book(book)

        elif command == "find-email":
            func.find_email(args, book)

        elif command == "del-email":
            func.del_email(args, book)
            func.save_book(book)

        elif command == "add-bday":
            func.add_bday(args, book)
            func.save_book(book)

        elif command == "del-bday":
            func.del_bday(args, book)
            func.save_book(book)

        elif command == "show-bday":
            func.show_bday(args, book)

        elif command == "add-adr":
            func.add_adr(args, book)
            func.save_book(book)

        elif command == "del-adr":
            func.del_adr(args, book)
            func.save_book(book)

        elif command == "find-adr":
            func.find_adr(args, book)

        elif command == "add-note":
            func.add_note(args, notes)
            func.save_notes(notes)

        elif command == "del-note":
            func.del_note(args, notes)
            func.save_notes(notes)

        elif command == "find-note":
            func.find_note(args, notes)

        elif command == "show-note":
            func.show_note(args, notes)

        elif command == "find-tag":
            func.find_tag(args, notes)

        elif command == "show-sorted-tags":
            func.show_sorted_tags(notes)

        else:
            print("Invalid command. Type 'help' for get a list of commands.")


if __name__ == "__main__":
    main()

{
    "Sally": {
        "name": {
            "value": "Sally"
        },
        "phones": [
            {
                "value": "(486)460040367698"
            }
        ],
        "emails": [],
        "address": {
            "value": "E5igrt6akn65k    "
        },
        "birthday": null
    },
    "Dawn": {
        "name": {
            "value": "Dawn"
        },
        "phones": [
            {
                "value": "(50)988715149"
            }
        ],
        "emails": [],
        "address": {
            "value": "Ov    uo0ew       46ehs   phct6gg8zeedzw6   2n7qqargrua37v07   1csj\t6ixotyzoinf\nglspne0nb2ectd\n2ui2iwrk8d7   te"
        },
        "birthday": {
            "value": "25.09.1998"
        }
    },
    "Paula": {
        "name": {
            "value": "Paula"
        },
        "phones": [
            {
                "value": "+642(3)070670237"
            }
        ],
        "emails": [
            {
                "value": "8y1ff@tdz1dyrl83.bfaf"
            },
            {
                "value": "g@ypkv1.eo"
            }
        ],
        "address": {
            "value": "Mbi\t    ozlslt5z64nx"
        },
        "birthday": {
            "value": "08.10.2011"
        }
    },
    "Samantha": {
        "name": {
            "value": "Samantha"
        },
        "phones": [
            {
                "value": "(111)8040947"
            }
        ],
        "emails": [],
        "address": {
            "value": "Ab\t       sbo0 sl1y5ht\tqrjy\np\nk4    7a7 res6bt396   2swh2xpyf9w5qf78j\n2a358"
        },
        "birthday": {
            "value": "31.12.1993"
        }
    },
    "Charles": {
        "name": {
            "value": "Charles"
        },
        "phones": [
            {
                "value": "1852567894882"
            }
        ],
        "emails": [
            {
                "value": "k2@88i9zfwch9.qow"
            }
        ],
        "address": {
            "value": "Vtafgjtri"
        },
        "birthday": {
            "value": "23.09.2020"
        }
    },
    "Roberta": {
        "name": {
            "value": "Roberta"
        },
        "phones": [],
        "emails": [],
        "address": null,
        "birthday": null
    },
    "Chris": {
        "name": {
            "value": "Chris"
        },
        "phones": [],
        "emails": [
            {
                "value": "qzzbb25s9@itntho6.dam"
            }
        ],
        "address": null,
        "birthday": {
            "value": "23.12.2004"
        }
    },
    "Barbara": {
        "name": {
            "value": "Barbara"
        },
        "phones": [],
        "emails": [],
        "address": null,
        "birthday": null
    },
    "Mary": {
        "name": {
            "value": "Mary"
        },
        "phones": [],
        "emails": [
            {
                "value": "2@3fu82.mlz"
            }
        ],
        "address": {
            "value": "Nm\n14    \n1    uj    sg16vfw1bscj772\nzwz    a0b   2rxtlb4n    vhx0ve1k1usv62uv9ve      u ql4takq    ma38b\t07gczit"
        },
        "birthday": {
            "value": "24.06.2003"
        }
    },
    "Matthew": {
        "name": {
            "value": "Matthew"
        },
        "phones": [
            {
                "value": "(83)3519909"
            }
        ],
        "emails": [],
        "address": null,
        "birthday": null
    },
    "Linda": {
        "name": {
            "value": "Linda"
        },
        "phones": [
            {
                "value": "7987453158691"
            }
        ],
        "emails": [],
        "address": {
            "value": "Gnyhhy5ueve3   9cf1j    un4hzdyi    a46dnarwe    c0\t\tktu\nl8u0aesr3el9j   q g3daf   p   cbmcbp   n\nb59i"
        },
        "birthday": {
            "value": "09.07.2009"
        }
    },
    "Susan": {
        "name": {
            "value": "Susan"
        },
        "phones": [
            {
                "value": "(761)4862570920"
            },
            {
                "value": "(0966)580505841295"
            }
        ],
        "emails": [
            {
                "value": "6aoqhgnaw@b4m0d.hkwha"
            },
            {
                "value": "tnfgsjs@6dlp.qugo"
            },
            {
                "value": "og@o5c8.yw"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Alissa": {
        "name": {
            "value": "Alissa"
        },
        "phones": [
            {
                "value": "+122(3603)38289731794016"
            },
            {
                "value": "(490)4237789544743"
            },
            {
                "value": "(661)9997909"
            }
        ],
        "emails": [
            {
                "value": "3m8hr@4li4g.ncqf"
            },
            {
                "value": "9a7@io5htlrv.dxv"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Carlton": {
        "name": {
            "value": "Carlton"
        },
        "phones": [
            {
                "value": "9241895"
            }
        ],
        "emails": [
            {
                "value": "c@arf09g.ui"
            },
            {
                "value": "my08@lt.ch"
            }
        ],
        "address": null,
        "birthday": {
            "value": "23.08.1952"
        }
    },
    "Dewey": {
        "name": {
            "value": "Dewey"
        },
        "phones": [],
        "emails": [
            {
                "value": "t@cf0.wux"
            }
        ],
        "address": {
            "value": "Qp3y   d35\t 2i6q8almd\t       90\n   a6d   d\tb27   j7y1y1do9ly7m   pnm60l7v\tw1o4 1v\t4\twond    15   rbq9hqg\nq4s"
        },
        "birthday": {
            "value": "12.08.2025"
        }
    },
    "Julie": {
        "name": {
            "value": "Julie"
        },
        "phones": [
            {
                "value": "(25)634407998666466"
            }
        ],
        "emails": [],
        "address": null,
        "birthday": {
            "value": "01.06.2020"
        }
    },
    "Terri": {
        "name": {
            "value": "Terri"
        },
        "phones": [],
        "emails": [],
        "address": null,
        "birthday": {
            "value": "15.02.2021"
        }
    },
    "Ruth": {
        "name": {
            "value": "Ruth"
        },
        "phones": [
            {
                "value": "1584320514823"
            },
            {
                "value": "+189(497)8268865266249"
            }
        ],
        "emails": [],
        "address": {
            "value": "Tpaswpzb l   0uo8m9r2    sq   8pq4 s3s53\t"
        },
        "birthday": {
            "value": "16.06.1961"
        }
    },
    "Anthony": {
        "name": {
            "value": "Anthony"
        },
        "phones": [
            {
                "value": "47111619392"
            }
        ],
        "emails": [
            {
                "value": "u9v2yzwp9@zghjmea7m1.xx"
            }
        ],
        "address": null,
        "birthday": {
            "value": "11.09.1955"
        }
    },
    "Tara": {
        "name": {
            "value": "Tara"
        },
        "phones": [
            {
                "value": "(81)6319213"
            }
        ],
        "emails": [],
        "address": {
            "value": "Zb79it7nblp0v6rh1xxs3ouxpalp4hbdms6gwvotypt hkb8ui5hl169ghn4\ththu\nsjh\t\t   4pfm   j"
        },
        "birthday": null
    },
    "Claire": {
        "name": {
            "value": "Claire"
        },
        "phones": [],
        "emails": [
            {
                "value": "557m14v1@4i5p.ogrf"
            },
            {
                "value": "grkka98n1@mvjo6r0a.gns"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Evelyn": {
        "name": {
            "value": "Evelyn"
        },
        "phones": [
            {
                "value": "(0016)01012613229"
            },
            {
                "value": "+68(95)79411383"
            }
        ],
        "emails": [],
        "address": {
            "value": "Hu05icm\t22461nt3p    v7hxk   mqzxsx2apzf67xhg7h bqjvu97m4t3 952       z"
        },
        "birthday": {
            "value": "06.09.1945"
        }
    },
    "Walter": {
        "name": {
            "value": "Walter"
        },
        "phones": [
            {
                "value": "(4735)676021655067"
            }
        ],
        "emails": [],
        "address": {
            "value": "Pxh69q\n5    v9m3hw9mk"
        },
        "birthday": {
            "value": "22.03.1957"
        }
    },
    "Van": {
        "name": {
            "value": "Van"
        },
        "phones": [],
        "emails": [],
        "address": {
            "value": "I    597ox wftst4    zjo z   a0fmqb9   2wgr0   wswn    79v0aq9 8s69imlghw1pnbtb24b 22c0w\tg   ke 9"
        },
        "birthday": {
            "value": "25.12.2000"
        }
    },
    "Kendrick": {
        "name": {
            "value": "Kendrick"
        },
        "phones": [
            {
                "value": "(955)860771065633"
            }
        ],
        "emails": [],
        "address": {
            "value": "I8m33\nmhza9ogfn4a6   hzxgu2wk75qgm"
        },
        "birthday": {
            "value": "06.06.1997"
        }
    },
    "David": {
        "name": {
            "value": "David"
        },
        "phones": [
            {
                "value": "+57226726710433"
            },
            {
                "value": "+311(2834)0946092688"
            }
        ],
        "emails": [],
        "address": {
            "value": "Xwii5wb8ivauvdsnxme   kjm79pgs    iuu2 o76y\nqh9n     b9"
        },
        "birthday": {
            "value": "03.06.1909"
        }
    },
    "Celeste": {
        "name": {
            "value": "Celeste"
        },
        "phones": [],
        "emails": [],
        "address": null,
        "birthday": {
            "value": "11.08.1959"
        }
    },
    "Wesley": {
        "name": {
            "value": "Wesley"
        },
        "phones": [
            {
                "value": "30171588667"
            }
        ],
        "emails": [],
        "address": null,
        "birthday": {
            "value": "23.09.2023"
        }
    },
    "Dorothy": {
        "name": {
            "value": "Dorothy"
        },
        "phones": [
            {
                "value": "(6153)443258910095893"
            },
            {
                "value": "+356602239230"
            },
            {
                "value": "+6(27)65335216847"
            }
        ],
        "emails": [
            {
                "value": "7uzxqcw@h9z.znadv"
            }
        ],
        "address": {
            "value": "K 34u\ng8   inc   jsqfqmq   55tbgyguz   iwq3h72r   fbkemsdj   a\njzwye    zul\tmi1"
        },
        "birthday": null
    },
    "Randy": {
        "name": {
            "value": "Randy"
        },
        "phones": [],
        "emails": [
            {
                "value": "a83ovkcvf@ho166.uq"
            },
            {
                "value": "cuo06tljib@t.zkj"
            }
        ],
        "address": null,
        "birthday": {
            "value": "21.12.1916"
        }
    },
    "Christine": {
        "name": {
            "value": "Christine"
        },
        "phones": [],
        "emails": [],
        "address": {
            "value": "Vea2h9xynpjcq\nw6hc8   ukxs4\nyjyw6\n5l   k2m2"
        },
        "birthday": {
            "value": "01.07.2004"
        }
    },
    "Kellie": {
        "name": {
            "value": "Kellie"
        },
        "phones": [
            {
                "value": "(1)62013923091"
            }
        ],
        "emails": [
            {
                "value": "df@b.ebcy"
            }
        ],
        "address": {
            "value": "Qjh   yrau31jq    y8t   586y\t62yc3 zk4\ty7ct0a05cm"
        },
        "birthday": null
    },
    "Lori": {
        "name": {
            "value": "Lori"
        },
        "phones": [
            {
                "value": "493593345"
            },
            {
                "value": "9074075"
            }
        ],
        "emails": [],
        "address": {
            "value": "Rf0\njbkax9s   u7vf5h3vz8l     5 5pwaf8yarmr4v    e99121sa        gfn57g3fko49a    u fb   x0u6eym4\tpr7      5d4usn"
        },
        "birthday": null
    },
    "Tammy": {
        "name": {
            "value": "Tammy"
        },
        "phones": [
            {
                "value": "310452229"
            },
            {
                "value": "+36652594116"
            }
        ],
        "emails": [
            {
                "value": "pk@m.bu"
            }
        ],
        "address": {
            "value": "C43ltf9ot\ntz\nk8 pdbsp1plqmu3tu0my1c5\n"
        },
        "birthday": {
            "value": "13.11.1921"
        }
    },
    "Raymond": {
        "name": {
            "value": "Raymond"
        },
        "phones": [
            {
                "value": "(5)152634374"
            }
        ],
        "emails": [],
        "address": {
            "value": "Zhmeq2nk7uwnvi 1"
        },
        "birthday": {
            "value": "07.09.2022"
        }
    },
    "Debbie": {
        "name": {
            "value": "Debbie"
        },
        "phones": [
            {
                "value": "+5(21)28422336686127"
            }
        ],
        "emails": [
            {
                "value": "xnan@kw3qppnj11.azapk"
            },
            {
                "value": "j@x1xurpw.ptv"
            },
            {
                "value": "whzfg1m@w.xmrji"
            }
        ],
        "address": {
            "value": "K53lg   vgv   \t    i6qt   hnh82\t\nd41x07va37\npns   ob18jqt3    p1p2d7inl5l    tf5w4uqab"
        },
        "birthday": null
    },
    "Gerry": {
        "name": {
            "value": "Gerry"
        },
        "phones": [
            {
                "value": "+48421392551"
            }
        ],
        "emails": [
            {
                "value": "feq@mbabtb.uq"
            },
            {
                "value": "z@8pu8sore.yot"
            }
        ],
        "address": null,
        "birthday": {
            "value": "22.09.2006"
        }
    },
    "Bonnie": {
        "name": {
            "value": "Bonnie"
        },
        "phones": [
            {
                "value": "+12(189)589612160931"
            },
            {
                "value": "(44)05479892939"
            },
            {
                "value": "+72823624185811"
            }
        ],
        "emails": [
            {
                "value": "ldy7gw@yjqz78gs.gf"
            }
        ],
        "address": null,
        "birthday": {
            "value": "12.04.2005"
        }
    },
    "Margaret": {
        "name": {
            "value": "Margaret"
        },
        "phones": [],
        "emails": [
            {
                "value": "110y@flei.nsavo"
            },
            {
                "value": "ba@q9pavihbrp.gnk"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Joan": {
        "name": {
            "value": "Joan"
        },
        "phones": [],
        "emails": [
            {
                "value": "esud@bf.ggccx"
            },
            {
                "value": "iozxfz@6kc.lhi"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Tina": {
        "name": {
            "value": "Tina"
        },
        "phones": [
            {
                "value": "133424254014"
            },
            {
                "value": "(82)429748985334"
            }
        ],
        "emails": [
            {
                "value": "b95dcp@40c9bs.heqr"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Justin": {
        "name": {
            "value": "Justin"
        },
        "phones": [
            {
                "value": "+55197459042"
            }
        ],
        "emails": [],
        "address": null,
        "birthday": {
            "value": "14.06.2028"
        }
    },
    "Billy": {
        "name": {
            "value": "Billy"
        },
        "phones": [
            {
                "value": "(87)135939138"
            }
        ],
        "emails": [
            {
                "value": "efl3kjui@enkyp.xikdq"
            },
            {
                "value": "13a@juiia.xyasb"
            },
            {
                "value": "2uzt7@la.vyrkq"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Carrie": {
        "name": {
            "value": "Carrie"
        },
        "phones": [
            {
                "value": "(49)43779256921233"
            }
        ],
        "emails": [],
        "address": null,
        "birthday": {
            "value": "08.07.2027"
        }
    },
    "Robert": {
        "name": {
            "value": "Robert"
        },
        "phones": [
            {
                "value": "3976604666"
            }
        ],
        "emails": [],
        "address": {
            "value": "Xfjso   qd6    rcnlfu\n41sq2p82s1faw\n88jt   kggt0g0jn"
        },
        "birthday": {
            "value": "22.04.2019"
        }
    },
    "Robin": {
        "name": {
            "value": "Robin"
        },
        "phones": [],
        "emails": [
            {
                "value": "1@9uta8.izjdo"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Harriet": {
        "name": {
            "value": "Harriet"
        },
        "phones": [],
        "emails": [],
        "address": {
            "value": "D   12q    m   8   iv8fe38q2dgb   4w8t   ngj03    6hen7o   m1t\n259eb\tby6nouklf9c2ppf9qg"
        },
        "birthday": {
            "value": "23.07.1908"
        }
    },
    "Andrew": {
        "name": {
            "value": "Andrew"
        },
        "phones": [],
        "emails": [
            {
                "value": "gl4u14@mune.cu"
            },
            {
                "value": "b0do@dgm4.kbsn"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Brian": {
        "name": {
            "value": "Brian"
        },
        "phones": [],
        "emails": [
            {
                "value": "ocl5@vlhialvzj.cnkl"
            },
            {
                "value": "zb4ztkx@bgch.swieq"
            },
            {
                "value": "xtsaap@mf9.tn"
            }
        ],
        "address": {
            "value": "V7o18    3gy20tye1bp 8u2uqf2e   lg4"
        },
        "birthday": {
            "value": "22.08.1940"
        }
    },
    "Dora": {
        "name": {
            "value": "Dora"
        },
        "phones": [
            {
                "value": "8462324"
            },
            {
                "value": "+553961360755046"
            }
        ],
        "emails": [],
        "address": null,
        "birthday": null
    },
    "Alexander": {
        "name": {
            "value": "Alexander"
        },
        "phones": [],
        "emails": [
            {
                "value": "ps@033vy.aj"
            }
        ],
        "address": null,
        "birthday": {
            "value": "23.09.1927"
        }
    },
    "Richard": {
        "name": {
            "value": "Richard"
        },
        "phones": [],
        "emails": [
            {
                "value": "nwx@ct.kpmy"
            }
        ],
        "address": {
            "value": "M\ncdx z9hy34a9rq588348bzxebm2ab9lhjtgskjq5aim04sotip\tqt\njr6rdvb    es2xa"
        },
        "birthday": null
    },
    "Greg": {
        "name": {
            "value": "Greg"
        },
        "phones": [
            {
                "value": "+16961832574"
            }
        ],
        "emails": [],
        "address": null,
        "birthday": null
    },
    "Hong": {
        "name": {
            "value": "Hong"
        },
        "phones": [
            {
                "value": "(80)6596995528315"
            },
            {
                "value": "(3)40519701213"
            }
        ],
        "emails": [
            {
                "value": "o7rt@8e9jvz7.yugp"
            }
        ],
        "address": null,
        "birthday": {
            "value": "23.11.2012"
        }
    },
    "Joey": {
        "name": {
            "value": "Joey"
        },
        "phones": [],
        "emails": [
            {
                "value": "o@zrc3.syd"
            },
            {
                "value": "vic@1r.naud"
            }
        ],
        "address": {
            "value": "T\n28umu5zt\n5vr\tah3m    m0i4o\n2rffot   s\nsvkpc    k0fhd10g1b   mrx30dspvg3agvbq33mm\t8p"
        },
        "birthday": null
    },
    "Mark": {
        "name": {
            "value": "Mark"
        },
        "phones": [
            {
                "value": "+32(06)08460969"
            },
            {
                "value": "9791048"
            }
        ],
        "emails": [],
        "address": {
            "value": "Upcd00ruu4tjjw ni2hti2m    xhnhcn5l"
        },
        "birthday": null
    },
    "Lucille": {
        "name": {
            "value": "Lucille"
        },
        "phones": [],
        "emails": [
            {
                "value": "e@l96n.lflau"
            },
            {
                "value": "jqf9gembo@ncer0927d5.gzl"
            },
            {
                "value": "mp50@e8c4y6.rhj"
            }
        ],
        "address": null,
        "birthday": {
            "value": "18.08.1919"
        }
    },
    "James": {
        "name": {
            "value": "James"
        },
        "phones": [
            {
                "value": "+85569400158277"
            },
            {
                "value": "+67924113048667120"
            }
        ],
        "emails": [],
        "address": {
            "value": "Q3k    yjv xp5x84atmspge   5utm74dbqd   \tgsty7dguuxs7lmazftx8\n4ux269 fc"
        },
        "birthday": null
    },
    "Diana": {
        "name": {
            "value": "Diana"
        },
        "phones": [
            {
                "value": "20413400"
            }
        ],
        "emails": [
            {
                "value": "p8uoh5@6n.re"
            }
        ],
        "address": {
            "value": "Oqkl\t3mr3rlnon   cv8mf9n\tot3pw      j47w"
        },
        "birthday": {
            "value": "23.02.1969"
        }
    },
    "Jennifer": {
        "name": {
            "value": "Jennifer"
        },
        "phones": [
            {
                "value": "686868044084"
            }
        ],
        "emails": [
            {
                "value": "4pvp@mxv.ihc"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Nathan": {
        "name": {
            "value": "Nathan"
        },
        "phones": [
            {
                "value": "(690)3777627497"
            },
            {
                "value": "(988)1810677"
            }
        ],
        "emails": [
            {
                "value": "t0nzjjcd6@m2wbhd3x.nkekq"
            }
        ],
        "address": null,
        "birthday": {
            "value": "31.10.1901"
        }
    },
    "Rachelle": {
        "name": {
            "value": "Rachelle"
        },
        "phones": [],
        "emails": [
            {
                "value": "s9fxkx75@zey8zcav.ux"
            }
        ],
        "address": {
            "value": "O\t0xa99brhsgj649opj2"
        },
        "birthday": null
    },
    "Eugene": {
        "name": {
            "value": "Eugene"
        },
        "phones": [
            {
                "value": "(1543)98756274"
            },
            {
                "value": "29209432227"
            }
        ],
        "emails": [
            {
                "value": "vzyhj@4qpxlznt1.zprmk"
            }
        ],
        "address": null,
        "birthday": {
            "value": "25.06.2019"
        }
    },
    "Thomas": {
        "name": {
            "value": "Thomas"
        },
        "phones": [
            {
                "value": "(31)1060107"
            }
        ],
        "emails": [],
        "address": {
            "value": "Fpd1pj4cdaajy8\t8lqd8i"
        },
        "birthday": null
    },
    "Betty": {
        "name": {
            "value": "Betty"
        },
        "phones": [
            {
                "value": "259159024589"
            }
        ],
        "emails": [
            {
                "value": "69oxleb7lu@tmn.iwf"
            }
        ],
        "address": {
            "value": "Om906961f478guco\tvabk8vgun\tj jyzq htkqwzei5j2my\tauqulo50uqq\n2ymhoivimcc"
        },
        "birthday": {
            "value": "01.08.2010"
        }
    },
    "Rose": {
        "name": {
            "value": "Rose"
        },
        "phones": [],
        "emails": [],
        "address": null,
        "birthday": {
            "value": "17.12.1914"
        }
    },
    "Sandra": {
        "name": {
            "value": "Sandra"
        },
        "phones": [],
        "emails": [
            {
                "value": "kq5dbizmhg@fi5agx.iaci"
            },
            {
                "value": "f9zvrd@y.guwj"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Lino": {
        "name": {
            "value": "Lino"
        },
        "phones": [
            {
                "value": "+73(3)226744618830"
            }
        ],
        "emails": [
            {
                "value": "1jv@uyjm6alc.vqdx"
            },
            {
                "value": "kc3ix@y4olp9.ni"
            }
        ],
        "address": null,
        "birthday": {
            "value": "17.10.2009"
        }
    },
    "Carl": {
        "name": {
            "value": "Carl"
        },
        "phones": [],
        "emails": [],
        "address": {
            "value": "Cf4d6r"
        },
        "birthday": null
    },
    "Kurt": {
        "name": {
            "value": "Kurt"
        },
        "phones": [],
        "emails": [
            {
                "value": "4fm6@vtnupsxn.elft"
            }
        ],
        "address": null,
        "birthday": {
            "value": "24.03.1936"
        }
    },
    "Serena": {
        "name": {
            "value": "Serena"
        },
        "phones": [],
        "emails": [],
        "address": {
            "value": "Qma1p401pg66\n   6x    dc4o\n88"
        },
        "birthday": null
    },
    "Rosie": {
        "name": {
            "value": "Rosie"
        },
        "phones": [
            {
                "value": "(156)2116323156"
            }
        ],
        "emails": [
            {
                "value": "wh30@ids6myy.kkczi"
            }
        ],
        "address": null,
        "birthday": null
    },
    "Jay": {
        "name": {
            "value": "Jay"
        },
        "phones": [],
        "emails": [],
        "address": {
            "value": "Yihpzc m6o 71j   \txx p8       8 j\tx   4jt\nru7k2e2jq   ouuu3auzk2   l\t1\nepjm   i35aov"
        },
        "birthday": null
    },
    "John": {
        "name": {
            "value": "John"
        },
        "phones": [
            {
                "value": "(403)70965008762452"
            }
        ],
        "emails": [],
        "address": {
            "value": "E5w   igeps\t6   8    j3jf872k 09vwk nniimc\txzb\nv284gnurb"
        },
        "birthday": {
            "value": "29.05.1984"
        }
    },
    "Tony": {
        "name": {
            "value": "Tony"
        },
        "phones": [],
        "emails": [
            {
                "value": "dlq58zzf@85h93n.mntjc"
            },
            {
                "value": "85us88d@bu5zcog.lyjl"
            }
        ],
        "address": {
            "value": "Cg\nroyi"
        },
        "birthday": {
            "value": "03.02.1930"
        }
    },
    "Sylvia": {
        "name": {
            "value": "Sylvia"
        },
        "phones": [],
        "emails": [],
        "address": null,
        "birthday": {
            "value": "07.02.2000"
        }
    },
    "Freddie": {
        "name": {
            "value": "Freddie"
        },
        "phones": [
            {
                "value": "(6)7135852129889"
            },
            {
                "value": "6339458555"
            },
            {
                "value": "(067)0466889834431"
            }
        ],
        "emails": [],
        "address": null,
        "birthday": null
    },
    "Kristal": {
        "name": {
            "value": "Kristal"
        },
        "phones": [
            {
                "value": "(1443)5919305"
            }
        ],
        "emails": [
            {
                "value": "7vzjktb0@d9xjhi6.cnypq"
            }
        ],
        "address": {
            "value": "Nx8    u5c16z   jswe8duom7i61s1slco8k   mn65y4t81co4w3plct6f8cg6    k3kfsrkp"
        },
        "birthday": null
    },
    "Sergio": {
        "name": {
            "value": "Sergio"
        },
        "phones": [
            {
                "value": "(5)886044813442540"
            },
            {
                "value": "1841440001"
            }
        ],
        "emails": [
            {
                "value": "zb12r6@0h77ld9.uodt"
            }
        ],
        "address": null,
        "birthday": {
            "value": "28.05.1972"
        }
    },
    "Shira": {
        "name": {
            "value": "Shira"
        },
        "phones": [
            {
                "value": "+468055369945206"
            }
        ],
        "emails": [],
        "address": {
            "value": "E0gf9n762l67\nlsb    pkwnc7sb46q    d4        b    a0w\n3wfg5gytrnwy   cs   22ezi7q"
        },
        "birthday": null
    },
    "Nick": {
        "name": {
            "value": "Nick"
        },
        "phones": [
            {
                "value": "(592)6017348219"
            },
            {
                "value": "8424390"
            }
        ],
        "emails": [
            {
                "value": "qb6t9@xwj22.zv"
            },
            {
                "value": "hfxz2@2khbmr.fpr"
            },
            {
                "value": "r@zh.aykp"
            }
        ],
        "address": {
            "value": "I   \n1zz32z    4d     megn0\t27t mjf   86i\nbod3icam0q   3 na\t   15vvfe6tk\ti3g9\tbqvfilf9kx   2cw\nb725pk    "
        },
        "birthday": null
    },
    "Shawn": {
        "name": {
            "value": "Shawn"
        },
        "phones": [
            {
                "value": "+862625970024"
            },
            {
                "value": "(578)1703653"
            },
            {
                "value": "+597049964372582"
            }
        ],
        "emails": [],
        "address": {
            "value": "Com   yb    9"
        },
        "birthday": {
            "value": "02.06.2013"
        }
    },
    "Anna": {
        "name": {
            "value": "Anna"
        },
        "phones": [],
        "emails": [],
        "address": null,
        "birthday": null
    },
    "Andrea": {
        "name": {
            "value": "Andrea"
        },
        "phones": [],
        "emails": [],
        "address": null,
        "birthday": null
    },
    "Erica": {
        "name": {
            "value": "Erica"
        },
        "phones": [
            {
                "value": "434837612793"
            }
        ],
        "emails": [
            {
                "value": "azrxzf@emw8zh94.xw"
            }
        ],
        "address": {
            "value": "Bcz1c\nkayg5l   k   un"
        },
        "birthday": {
            "value": "07.03.2015"
        }
    },
    "Elizabeth": {
        "name": {
            "value": "Elizabeth"
        },
        "phones": [
            {
                "value": "(29)4162891"
            },
            {
                "value": "73686210"
            },
            {
                "value": "(924)00781974"
            }
        ],
        "emails": [],
        "address": {
            "value": "Nj \tzm9u1p          ufvf3sv   d9fah275axl   zd\t36\ts6mtwlra2g8qv0    qlx2c86gz"
        },
        "birthday": null
    }
}