import json
from django.shortcuts import render
from django.http import JsonResponse, response
from .models import LastAdmNo, Temp,Courses,StudDetails,Tc,Cc
from datetime import datetime
# Create your views here.




def verification(request):
    if request.method=='POST':
        context={
        'tempdata':Temp.objects.filter(temp_no=request.POST['tmp_no']).first()
        }
        return render(request,'office/verification.html',context)
       # print(tempdata)
    return render(request,'office/verification.html')

def fetch_coursename(request):
    courseid = request.GET.get('courseid', None)
    values = Courses.objects.filter(id__iexact=courseid).first()
    values = values.__dict__
    
    data = {
        'coursename': values['course']
        
    }
    print(data)
    return JsonResponse(data)









def admnn_no_gen(request):
    if request.method=='POST':
        tempdata = Temp.objects.filter(temp_no=request.POST['tmp_no']).first()

        

        now = datetime.now()
        year = now.strftime("%Y")
        yr=year[2:4]					
            
            #for generating Admission number last 2 digits is taken from the current year...

        if((request.POST['course1'] =='BTECH')or(request.POST['course1'] == 'BARCH')):
            lastadm =LastAdmNo.objects.all()
            obj_lastadm=lastadm.get()
            stid = obj_lastadm[0]
            next_stid =stid + 1

         			#incrementing the UG value in the last_adm_no table...

            if((request.POST['course1'] == 'BTECH')and(tempdata.branch_or_specialisation == 'CIVIL ENGINEERING')):
                code="BC"
         
            elif((request.POST['course1'] == 'BTECH')and(tempdata.branch_or_specialisation == 'MECHANICAL ENGINEERING')):
                code="BM"
           
            elif((request.POST['course1'] == 'BTECH')and(tempdata.branch_or_specialisation == 'ELECTRICAL AND ELECTRONICS ENGINEERING')):
                code="BE"
            
            elif((request.POST['course1'] == 'BTECH')and(tempdata.branch_or_specialisation == 'ELECTRONICS AND COMMUNICATION ENGINEERING')):
                code="BL"
           
            elif((request.POST['course1'] == 'BTECH')and(tempdata.branch_or_specialisation == 'COMPUTER SCIENCE AND ENGINEERING')):
                code="BR"
            
            elif((request.POST['course1'] == 'BARCH')and(tempdata.branch_or_specialisation == 'ARCHITECTURE')):
                code="BA"
            
        admission_num = yr+code+next_stid                      
           #genarating admission number for UG students......
        

        if((request.POST['course1'] == 'MTECH')or(request.POST['course1'] == 'MCA')):
        
            lastadm =LastAdmNo.objects.all()
            obj_lastadm=lastadm.pg()
            st_id1 = obj_lastadm[0]
            nextst_id1=st_id1+1									
            	#incrementing the PG value in the last_adm_no table...

            if((request.POST['course1'] == 'MTECH')and(tempdata.branch_or_specialisation== 'INDUSTRIAL ENGINEERING AND MANAGEMENT')):
                code="MM"
            if((request.POST['course1'] == 'MTECH')and(tempdata.branch_or_specialisation == 'INDUSTRICAL DRIVES AND CONTROL')):
                code="ME"
            if((request.POST['course1'] == 'MTECH')and(tempdata.branch_or_specialisation == 'TRANSPORTATION ENGINEERING')):
                code="MC"
            if((request.POST['course1'] == 'MTECH')and(tempdata.branch_or_specialisation == 'MECHANICAL ENGINEERING')):
                code="MME"
            if((request.POST['course1'] == 'MTECH')and(tempdata.branch_or_specialisation == 'ADVANCED COMMUNICATION AND INFORMATION SYSTEM')):
                code="ML"
            if((request.POST['course1'] == 'MTECH')and(tempdata.branch_or_specialisation == 'ADVANCED ELECTRONICS AND COMMUNICATION')):
                code="ML"
            if((request.POST['course1'] == 'MTECH')and(tempdata.branch_or_specialisation == 'COMPUTER SCIENCE AND ENGINEERING')):
                code="MR"  

            if((request.POST['course1'] == 'MCA')and(tempdata.branch_or_specialisation == 'COMPUTER APPLICATIONS')):
                code="MP"
            
        admission_num=yr+code+nextst_id1										
        	#genarating admission number for PG students......

         
       # print(admission_num)
    return render(request,'office/verification.html',admission_num)




def verify(request):
    
    if request.method=='POST':
        
	
       

        studdata = StudDetails( admissionno = request.POST['adm_no'],name = request.POST['name'],year_of_admission = request.POST['dte'],blood = request.POST['blood'],mobile_phno = request.POST['mobile'],
        branch_or_specialisation = request.POST['spec'],email = request.POST['email'],admission_type = request.POST['admtype'],
        status = request.POST['studstatus'],address = request.POST['address'],land_phno  = request.POST['phone'],rollno = request.POST['roll_num'],
        rank  = request.POST['rank_no'],quota  = request.POST['quota'],school_1  = request.POST['school_1'],regno_1  = request.POST['reg_no_yr_1'],board_1 = request.POST['board_1'],
        percentage_1  = request.POST['per1'],school_2  = request.POST['school_2'], regno_2 = request.POST['reg_no_yr_2'],  board_2  = request.POST['board_2'],
        percentage_2  = request.POST['per2'],no_chance1  = request.POST['no_chance'], gender = request.POST['gender'],)
        

        studdata.save()


        return render(request,'office/verification.html')
       # print(tempdata)
    return render(request,'office/verification.html')









def tc(request):
    if request.method=='POST':
        context1={
        'studdata':StudDetails.objects.filter(admissionno=request.POST['a_no']).first(),
        'tcdata':Tc.objects.filter(adm_no=request.POST['a_no']).first()

        }
        return render(request,'office/transfer_certificate.html',context1)
        
    return render(request,'office/transfer_certificate.html')




def cc(request):
    if request.method=='POST':
        context1={
        'studdata':StudDetails.objects.filter(admissionno=request.POST['a_no']).first(),
        'tcdata':Tc.objects.filter(adm_no=request.POST['a_no']).first(),
        'ccdata':Cc.objects.filter(adm_no=request.POST['a_no']).first(),
        #'coursedata':Courses.objects.filter(adm_no=request.POST['a_no']).first(),

        }
        return render(request,'office/conduct_certificate.html',context1)
        
    return render(request,'office/conduct_certificate.html')



#def fetch_tcno(request):
    #admno = request.GET.get('courseid', None)
    #values = Tc.objects.filter(adm_no__iexact=admno).first()
    #values = values.__dict__
    
    #data = {
        #'tcnum': values['tc_no']
        
    #}
    #print(data)
    #return JsonResponse(data)









def sem_verification(request):

     if request.method=='POST':
        context2={
        'students':StudDetails.objects.filter(admissionno=request.POST['add_no']).first()
        }
        #return render(request,'office/student_search.html',context2)
        print(context2)

     return render(request,'office/student_search.html')




















def search(request):

    if request.method=='POST':

        return render(request,'office/student_search.html')
    return render(request,'office/student_search.html')






def backend_search(request):
    if request.method=='GET':
        number=request.GET['add_no']
              
                                    #print("oneshot")
        if number is not None:
                                    #print(request.POST['add_no'])
            studobjects=StudDetails.objects.filter(admissionno__startswith=number)
            data=[]
            for studobj in studobjects:
                stud=studobj.__dict__
                data.append(stud['admissionno'])
                                    #studobjects= studobjects.__dict__
                                    #data= {
                                            #'add_no':stud['admissionno'] }
                                    #count=StudDetails.objects.filter(admissionno=request.POST['add_no']).count()
                                    #if count>0:
                                        #data= {
                                            #'studobjects':studobjects }
                                    #for row in studobjects:
                                        #print(row['admissionno'])
                                    #else:
                                        #print("No matches found..")

            print(data)
        

    return JsonResponse({'aaaa':data})
                                    
                        
def backend_search2(request):
    if request.method=='GET':
        number1=request.GET['name']
              
                                    #print("oneshot")
        if number1 is not None:
                                    #print(request.POST['add_no'])
            studobjects=StudDetails.objects.filter(name__startswith=number1)
            data=[]
            for studobj in studobjects:
                stud=studobj.__dict__
                data.append(stud['name'])
                                    #studobjects= studobjects.__dict__
                                    #data= {
                                            #'add_no':stud['admissionno'] }
                                    #count=StudDetails.objects.filter(admissionno=request.POST['add_no']).count()
                                    #if count>0:
                                        #data= {
                                            #'studobjects':studobjects }
                                    #for row in studobjects:
                                        #print(row['admissionno'])
                                    #else:
                                        #print("No matches found..")

            print(data)

    return JsonResponse({'aaaa':data})           
        
       
def backend_search3(request):
    if request.method=='POST':
        number2 = request.POST['add_no']
        if number2 is not None:
            studobjects2=StudDetails.objects.filter(admissionno =number2).first()
            result=[]
            for studobjct in studobjects2:
                stud=studobjct.__dict__
                result.append(stud['admissionno','name'],stud['name'],stud['dob'],stud['gender'],stud['religion'],stud['caste'],stud['year_of_admission'],stud['email '],stud['mobile_phno '])
            
            print(result)
    return response({'result':result})
   













