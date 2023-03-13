import uuid
import time
class task_field:
    def __init__(self,id,task,created_time,updated_time='NA',complete_task=False,task_done='NA'):
            self.id = id
            self.task = task
            self.created_time = created_time
            self.updated_time = updated_time
            self.complete_task = complete_task
            self.task_done = task_done

class Task:
    work = []
    def add_tsk(self):
        add_task = input('Enter task: ')
        id = uuid.uuid4()
        c_time = time.ctime()
        self.all_val = task_field(id,add_task,c_time)
        self.work.append(vars(self.all_val))
        print('\nTask add successfully!\n')

    def show_all_task(self):
         for t in self.work:
            for key,v in t.items():
                print(key,':',v)

            print('\n')

    def update_task(self):
        for i,t in enumerate(self.work):
            print('task-no: ',i+1)
            for key,v in t.items():
                print(key,':',v)
            print('\n')
  
        task_no = int(input('Enter task no: '))
        name = input('Enter new task: ')
        up_time = time.ctime()
        flag = False
        for i,t in enumerate(self.work):
            if(i==task_no-1):
                for key,v in t.items():
                    if(self.work[i]['complete_task']!=True):
                        # name = input('Enter new task: ')
                        self.work[i]['task'] = name
                        self.work[i]['updated_time'] = up_time
                        flag = True
        if(flag==False):
            print('\nTask already complete!\n')
        else:
            print('\nTask Updated successfully!\n')

    def mark_complete(self):
        for i,t in enumerate(self.work):
            print('task-no: ',i+1)
            for key,v in t.items():
                print(key,':',v)
            print('\n')

        for_complete =int(input('Enter task no: '))
        flag = False
        for i,t in enumerate(self.work):
            if(i==for_complete-1):
                for key,v in t.items():
                    if(self.work[i]['complete_task']==False):
                        complete_time = time.ctime()
                        self.work[i]['complete_task'] = True
                        self.work[i]['task_done'] = complete_time
                        flag = True
        if(flag==False):
            print('\nTask has already comcleted!\n')
        else:
            print('\nTask Completed successfully!\n')
                   
    def complete_task(self): 
        for i,t in enumerate(self.work):
                for key,v in t.items():
                  if (self.work[i]['complete_task'] == True):
                         print(key,':',v)
                print('\n')
    
    def show_incomplete_task(self): 
        for i,t in enumerate(self.work):
            for key,v in t.items():
                if (self.work[i]['complete_task'] == False):
                        print(key,':',v)
            print('\n')

t = Task()

while(True):
    print('1.Add new Task\n2.Show all task\n3.Show incomplete Task\n4.Show complete Task\n5.Update Task\n6.Mark a Task complete')

    op = input('Enter op: ')
    print('\n')
    if(op=='1'):
        t.add_tsk()
    elif(op=='2'):
         t.show_all_task()
    elif(op=='5'):
       t.update_task()
    elif(op=='6'):
        t.mark_complete()
    elif(op=='4'):
        t.complete_task()
    elif(op=='3'):
        t.show_incomplete_task()


