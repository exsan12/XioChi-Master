'''
Module Exploit And Exploit With Metasploit Framework
Created by ~xGans
Facebook : https://web.facebook.com/ichsan.AndroSec
Gmail : Exsandrrt01@gmail.com
you can report bug on my email
'''
import requests
import subprocess
import sys
from core import log
from core import wcolors
#wordlist by ExploreCrew.org | IBT Riau | Bob Halliwel(Thx buat listing exploit-idnya) | AVP
a1 = 'wp-content/plugins/portable-phpmyadmin/wp-pma-mod <=> (The Exploit Is)> http://www.exploit-db.com/exploits/23356/'
a2 = 'wp-content/themes/clockstone/theme/functions/upload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/23494/'
a3 = 'wp-content/plugins/plugin-dir/timeline/index.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/22853/'
a4 = 'wp-content/plugins/all-video-gallery/config.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/22427/'
a5 = 'wp-content/plugins/bbpress/forum.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/22396/'
a6 = 'wp-content/plugins/foxypress/uploadify/uploadify.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/22374/'
a7 = 'wp-admin/post.php?post=43&action=edit <=> (The Exploit Is)> http://www.exploit-db.com/exploits/22374/'
a8 = 'wp-content/plugins/webinar_plugin/get-widget.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/22300/'
a9 = 'wp-content/plugins/webinar_plugin/get-widget.php?wid=3 <=> (The Exploit Is)> http://www.exploit-db.com/exploits/22300/'
a10 = 'wp-content/plugins/social-discussions/social-discussions-networkpub_ajax.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/22158/'
a11 = 'wp-content/plugins/fs-real-estate-plugin/xml/marker_listings.xml?id=<=> (The Exploit Is)> http://www.exploit-db.com/exploits/22071/'
a12 = 'wp-content/themes/archin/hades_framework/option_panel/ajax.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/21646/'
a13 = 'wp-admin/admin.php?page=wp-topbar.php&action=topbartext&barid=1 <=> (The Exploit Is)> http://www.exploit-db.com/exploits/21393/'
a14 = 'wp-content/plugins/hd-webplayer/config.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/20918/'
a15 = 'wp-content/plugins/hd-webplayer/playlist.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/20918/'
a16 = 'wp-content/plugins/count-per-day/ <=> (The Exploit Is)> http://www.exploit-db.com/exploits/20862/'
a17 = 'wp-content/plugins/mini-mail-dashboard-widget/ <=> (The Exploit Is)> http://www.exploit-db.com/exploits/20358/'
a18 = 'wp-content/plugins/postie/ <=> (The Exploit Is)> http://www.exploit-db.com/exploits/20360/'
a19 = 'wp-content/plugins/wp-simplemail/ <=> (The Exploit Is)> http://www.exploit-db.com/exploits/20361/'
a20 = 'wp-content/plugins/threewp-email-reflector/ <=> (The Exploit Is)> http://www.exploit-db.com/exploits/20365/'
a21 = 'wp-content/themes/diary/sendmail.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19862/'
a22 = 'wp-content/plugins/resume-submissions-job-postings/includes/functions.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19791/'
a23 = 'wp-content/plugins/website-faq/website-faq-widget.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19400/'
a24 = 'wp-content/plugins/radykal-fancy-gallery/admin/image-upload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19398/'
a25 = 'wp-content/plugins/wp-automatic/inc/csv.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19187/'
a26 = 'wp-content/plugins/wp-gpx-maps/wp-gpx-maps_admin_tracks.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19050/'
a27 = 'wp-content/plugins/user-meta/framework/helper/uploader.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19052/'
a28 = 'wp-content/plugins/topquark/lib/js/fancyupload/showcase/batch/script.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19053/'
a29 = 'wp-content/plugins/sfbrowser/connectors/php/sfbrowser.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19054/'
a30 = 'wp-content/plugins/pica-photo-gallery/picaPhotosResize.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19055/'
a31 = 'wp-content/plugins/mac-dock-gallery/upload-file.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19056/'
a32 = 'wp-content/plugins/drag-drop-file-uploader/dnd-upload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19057/'
a33 = 'wp-content/plugins/custom-content-type-manager/upload_form.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19058/'
a34 = 'wp-content/plugin/content-flow3d <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19036/'
a35 = 'wp-content/plugins/front-file-manager/upload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19012/'
a36 = 'wp-content/plugins/pica-photo-gallery/picadownload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19016/'
a37 = 'wp-content/plugins/plugin-newsletter/preview.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19018/'
a38 = 'wp-content/plugins/rbxgallery/uploader.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19019/'
a39 = 'wp-content/plugins/simple-download-button-shortcode/simple-download-button_dl.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19020/'
a40 = 'wp-content/plugins/thinkun-remind/exportData.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19021/'
a41 = 'wp-content/plugins/tinymce-thumbnail-gallery/php/download-image.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19022/'
a42 = 'wp-content/plugins/wpstorecart/php/upload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19023/'
a43 = 'wp-content/plugins/omni-secure-files/plupload/examples/upload.php <=> (The Exploit Is)> www.exploit-db.com/exploits/19009/'
a44 = 'wp-content/plugins/front-end-upload/upload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/19008/'
a45 = 'wp-content/plugins/gallery-plugin/upload/php.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18998/'
a46 = 'wp-content/plugins/mm-forms-community/includes/doajaxfileupload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18997/'
a47 = 'wp-content/plugins/font-uploader/font-upload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18994/'
a48 = 'wp-content/plugins/mm-forms-community/includes/doajaxfileupload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18997/'
a49 = 'wp-content/plugins/gallery-plugin/upload/php.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18998/'
a50 = 'wp-content/plugins/asset-manager/upload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18993/'
a51 = 'wp-content/plugins/font-uploader/font-upload.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18994/'
a52 = 'wp-content/plugins/foxypress/uploadify/uploadify.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18991/'
a53 = 'wp-content/plugins/html5avmanager/lib/uploadify/custom.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18990/'
a54 = 'wp-content/plugins/store-locator-le/core/load_wp_config.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18989/'
a55 = 'wp-content/plugins/wpmarketplace/uploadify/uploadify.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18988/'
a56 = 'wp-content/plugins/wp-property/third-party/uploadify/uploadify.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18987/'
a57 = 'wp-content/plugins/kish-guest-posting/uploadify/scripts/uploadify.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18412/'
a58 = 'wp-content/plugins/ucan-post/ <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18390/'
a59 = 'wp-content/plugins/count-per-day/download.php?n=<=> (The Exploit Is)> http://www.exploit-db.com/exploits/18355/'
a60 = 'wp-content/plugins/wp-autoyoutube/modules/index.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18353/'
a61 = 'wp-content/plugins/age-verification/age-verification.php?redirect_to= <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18350/'
a62 = 'wp-content/plugins/pay-with-tweet.php/pay.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18330/'
a63 = 'wp-content/plugins/mailz/lists/dl.php? <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18276/'
a64 = 'wp-admin/admin-ajax.php? <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18231/'
a65 = 'wp-content/plugins/jetpack/modules/sharedaddy.php <=> (The Exploit Is)> http://www.exploit-db.com/exploits/18126/'
a66 = 'wp-content/plugins/adrotate/adrotate-out.php?track=<=> (The Exploit Is)> http://www.exploit-db.com/exploits/18114/'

def wpvuln(target):
    count = 1
    wppayload = open('core/wordlist/wp.txt', 'r')
    s = target
    for i in wppayload.readlines():
        d = s + str(i)
        try:
            r = requests.get(d)
            cunt = 'a%s'%(count)
            count += 1
            status = r.status_code
            print(wcolors.color.CYAN+30 * '#')

            if r.status_code in (200,301):
                log.logger.attack("Exploit Found!!")
                log.logger.attacksukses1("Target", s)
                if cunt == 'a1':
                    log.logger.attacksukses1("Path>> ", "/"+a1)
                if cunt == 'a2':
                    log.logger.attacksukses1("Path>> ", "/"+a2)
                if cunt == 'a3':
                    log.logger.attacksukses1("Path>> ", "/"+a3)
                if cunt == 'a4':
                    log.logger.attacksukses1("Path>> ", "/"+a4)
                if cunt == 'a5':
                    log.logger.attacksukses1("Path>> ", "/"+a5)
                if cunt == 'a6':
                    log.logger.attacksukses1("Path>> ", "/"+a6)
                if cunt == 'a7':
                    log.logger.attacksukses1("Path>> ", "/"+a7)
                if cunt == 'a8':
                    log.logger.attacksukses1("Path>> ", "/"+a8)
                if cunt == 'a9':
                    log.logger.attacksukses1("Path>> ", "/"+a9)
                if cunt == 'a10':
                    log.logger.attacksukses1("Path>> ", "/"+a10)
                if cunt == 'a11':
                    log.logger.attacksukses1("Path>> ", "/"+a11)
                if cunt == 'a12':
                    log.logger.attacksukses1("Path>> ", "/"+a12)
                if cunt == 'a13':
                    log.logger.attacksukses1("Path>> ", "/"+a13)
                if cunt == 'a14':
                    log.logger.attacksukses1("Path>> ", "/"+a14)
                if cunt == 'a15':
                    log.logger.attacksukses1("Path>> ", "/"+a15)
                if cunt == 'a16':
                    log.logger.attacksukses1("Path>> ", "/"+a16)
                if cunt == 'a17':
                    log.logger.attacksukses1("Path>> ", "/"+a17)
                if cunt == 'a18':
                    log.logger.attacksukses1("Path>> ", "/"+a18)
                if cunt == 'a19':
                    log.logger.attacksukses1("Path>> ", "/"+a19)
                if cunt == 'a20':
                    log.logger.attacksukses1("Path>> ", "/"+a20)
                if cunt == 'a21':
                    log.logger.attacksukses1("Path>> ", "/"+a21)
                if cunt == 'a22':
                    log.logger.attacksukses1("Path>> ", "/"+a22)
                if cunt == 'a23':
                    log.logger.attacksukses1("Path>> ", "/"+a23)
                if cunt == 'a24':
                    log.logger.attacksukses1("Path>> ", "/"+a24)
                if cunt == 'a25':
                    log.logger.attacksukses1("Path>> ", "/"+a25)
                if cunt == 'a26':
                    log.logger.attacksukses1("Path>> ", "/"+a26)
                if cunt == 'a27':
                    log.logger.attacksukses1("Path>> ", "/"+a27)
                if cunt == 'a28':
                    log.logger.attacksukses1("Path>> ", "/"+a28)
                if cunt == 'a29':
                    log.logger.attacksukses1("Path>> ", "/"+a29)
                if cunt == 'a30':
                    log.logger.attacksukses1("Path>> ", "/"+a30)
                if cunt == 'a31':
                    log.logger.attacksukses1("Path>> ", "/"+a31)
                if cunt == 'a32':
                    log.logger.attacksukses1("Path>> ", "/"+a32)
                if cunt == 'a33':
                    log.logger.attacksukses1("Path>> ", "/"+a33)
                if cunt == 'a34':
                    log.logger.attacksukses1("Path>> ", "/"+a34)
                if cunt == 'a35':
                    log.logger.attacksukses1("Path>> ", "/"+a35)
                if cunt == 'a36':
                    log.logger.attacksukses1("Path>> ", "/"+a36)
                if cunt == 'a37':
                    log.logger.attacksukses1("Path>> ", "/"+a37)
                if cunt == 'a38':
                    log.logger.attacksukses1("Path>> ", "/"+a38)
                if cunt == 'a39':
                    log.logger.attacksukses1("Path>> ", "/"+a39)
                if cunt == 'a40':
                    log.logger.attacksukses1("Path>> ", "/"+a40)
                if cunt == 'a41':
                    log.logger.attacksukses1("Path>> ", "/"+a41)
                if cunt == 'a42':
                    log.logger.attacksukses1("Path>> ", "/"+a42)
                if cunt == 'a43':
                    log.logger.attacksukses1("Path>> ", "/"+a43)
                if cunt == 'a44':
                    log.logger.attacksukses1("Path>> ", "/"+a44)
                if cunt == 'a45':
                    log.logger.attacksukses1("Path>> ", "/"+a45)
                if cunt == 'a46':
                    log.logger.attacksukses1("Path>> ", "/"+a46)
                if cunt == 'a47':
                    log.logger.attacksukses1("Path>> ", "/"+a47)
                if cunt == 'a48':
                    log.logger.attacksukses1("Path>> ", "/"+a48)
                if cunt == 'a49':
                    log.logger.attacksukses1("Path>> ", "/"+a49)
                if cunt == 'a50':
                    log.logger.attacksukses1("Path>> ", "/"+a50)
                if cunt == 'a51':
                    log.logger.attacksukses1("Path>> ", "/"+a51)
                if cunt == 'a52':
                    log.logger.attacksukses1("Path>> ", "/"+a52)
                if cunt == 'a53':
                    log.logger.attacksukses1("Path>> ", "/"+a53)
                if cunt == 'a54':
                    log.logger.attacksukses1("Path>> ", "/"+a54)
                if cunt == 'a55':
                    log.logger.attacksukses1("Path>> ", "/"+a55)
                if cunt == 'a56':
                    log.logger.attacksukses1("Path>> ", "/"+a56)
                if cunt == 'a57':
                    log.logger.attacksukses1("Path>> ", "/"+a57)
                if cunt == 'a58':
                    log.logger.attacksukses1("Path>> ", "/"+a58)
                if cunt == 'a59':
                    log.logger.attacksukses1("Path>> ", "/"+a59)
                if cunt == 'a60':
                    log.logger.attacksukses1("Path>> ", "/"+a60)
                if cunt == 'a61':
                    log.logger.attacksukses1("Path>> ", "/"+a61)
                if cunt == 'a62':
                    log.logger.attacksukses1("Path>> ", "/"+a62)
                if cunt == 'a63':
                    log.logger.attacksukses1("Path>> ", "/"+a63)
                if cunt == 'a64':
                    log.logger.attacksukses1("Path>> ", "/"+a64)
                if cunt == 'a65':
                    log.logger.attacksukses1("Path>> ", "/"+a65)
                if cunt == 'a66':
                    log.logger.attacksukses1("Path>> ", "/"+a66)
                print(wcolors.color.CYAN+30 * '#')
                print ""
            else:
                log.logger.error1("NotFound", d)
                log.logger.error1("Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
                print ""
        except KeyboardInterrupt:
                print "Exit"
def cgivuln(target):
    cgipayload = open('core/wordlist/cgi.txt', 'r')
    s = target
    for i in cgipayload.readlines():
        d = s + str(i)
        try:

            r = requests.get(d)
            status = r.status_code
            if status in (200,301):
                print(wcolors.color.CYAN+30 * '#')
                log.logger.attacksukses1("Found", d)
                log.logger.attacksukses1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
            else:
                print(wcolors.color.CYAN+30 * '#')
                log.logger.error1("NotFound", d)
                log.logger.error1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
        except requests.exceptions.ConnectionError:
            log.logger.error1("Some Error Found", "you forgot </> on last url")
            break
        except KeyboardInterrupt:
            log.logger.error1("Thx For Using :) Xiochi", "Exsan :) Dicky :) Hendriawan :)")
def dirtraversalwin(target):
    travwinpayload = open('core/wordlist/dirTraversal-win.txt', 'r')
    s = target
    for i in travwinpayload.readlines():
        d = s + str(i)
        try:

            r = requests.get(d)
            status = r.status_code
            if status in (200,301):
                print(wcolors.color.CYAN+30 * '#')
                log.logger.attacksukses1("Found", d)
                log.logger.attacksukses1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
            else:
                print(wcolors.color.CYAN+30 * '#')
                log.logger.error1("NotFound", d)
                log.logger.error1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
        except requests.exceptions.ConnectionError:
            log.logger.error1("Some Error Found", "you forgot </> on last url")
            break
        except KeyboardInterrupt:
            log.logger.error1("Thx For Using :) Xiochi", "Exsan :) Dicky :) Hendriawan :)")
def dirtraversalunix(target):
    travnixpayload = open('core/wordlist/dirTraversal-nix.txt', 'r')
    s = target
    for i in travnixpayload.readlines():
        d = s + str(i)
        try:

            r = requests.get(d)
            status = r.status_code
            if status in (200,301):
                print(wcolors.color.CYAN+30 * '#')
                log.logger.attacksukses1("Found", d)
                log.logger.attacksukses1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
            else:
                print(wcolors.color.CYAN+30 * '#')
                log.logger.error1("NotFound", d)
                log.logger.error1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
        except requests.exceptions.ConnectionError:
            log.logger.error1("Some Error Found", "you forgot </> on last url")
            break
        except KeyboardInterrupt:
            log.logger.error1("Thx For Using :) Xiochi", "Exsan :) Dicky :) Hendriawan :)")
def weblogic(target):
    weblogicpayload = open('core/wordlist/weblogic.txt', 'r')
    s = target
    for i in weblogicpayload.readlines():
        d = s + str(i)
        try:

            r = requests.get(d)
            status = r.status_code
            if status in (200,301):
                print(wcolors.color.CYAN+30 * '#')
                log.logger.attacksukses1("Found", d)
                log.logger.attacksukses1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
            else:
                print(wcolors.color.CYAN+30 * '#')
                log.logger.error1("NotFound", d)
                log.logger.error1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
        except requests.exceptions.ConnectionError:
            log.logger.error1("Some Error Found", "you forgot </> on last url")
            break
        except KeyboardInterrupt:
            log.logger.error1("Thx For Using :) Xiochi", "Exsan :) Dicky :) Hendriawan :)")
def apache(target):
    apachepayload = open('core/wordlist/apache.txt', 'r')
    s = target
    for i in apachepayload.readlines():
        d = s + str(i)
        try:

            r = requests.get(d)
            status = r.status_code
            if status in (200,301):
                print(wcolors.color.CYAN+30 * '#')
                log.logger.attacksukses1("Found", d)
                log.logger.attacksukses1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
            else:
                print(wcolors.color.CYAN+30 * '#')
                log.logger.error1("NotFound", d)
                log.logger.error1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
        except requests.exceptions.ConnectionError:
            log.logger.error1("Some Error Found", "you forgot </> on last url")
            break
        except KeyboardInterrupt:
            log.logger.error1("Thx For Using :) Xiochi", "Exsan :) Dicky :) Hendriawan :)")
def tomcat(target):
    tomcatpayload = open('core/wordlist/tomcat.txt', 'r')
    s = target
    for i in tomcatpayload.readlines():
        d = s + str(i)
        try:

            r = requests.get(d)
            status = r.status_code
            if status in (200,301):
                print(wcolors.color.CYAN+30 * '#')
                log.logger.attacksukses1("Found", d)
                log.logger.attacksukses1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
            else:
                print(wcolors.color.CYAN+30 * '#')
                log.logger.error1("NotFound", d)
                log.logger.error1("With Status Code", status)
                print(wcolors.color.CYAN+30 * '#')
        except requests.exceptions.ConnectionError:
            log.logger.error1("Some Error Found", "you forgot </> on last url")
            break
        except KeyboardInterrupt:
            log.logger.error1("Thx For Using :) Xiochi", "Exsan :) Dicky :) Hendriawan :)")
