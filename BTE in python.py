def estimate(act_bt,a,e_0):
    pred_bt=[e_0]
    for i in range(1,len(act_bt)):
        prev_pred=pred_bt[-1]
        pred=a*act_bt[i-1]+(1-a)*prev_pred
        pred_bt.append(pred)
    return pred_bt

act_bt=[]
n=int(input("enter no. of processes: "))
print("enter burst time of each process: ")
for i in range(n):
    bt=float(input(f"Process {i+1}: "))
    act_bt.append(bt)

e_0=float(input("enter the initial predicted burst time: "))

a=float(input("enter smooothing factor (0<=a<=1): "))

pred_bt=estimate(act_bt,a,e_0)

print("\nProcess\tActual_BT Predicted_BT")
print("-----------------------------------------")
for i in range(n):
    print("P",i,"\t",act_bt[i],"\t    ",pred_bt[i],(" (Previous Prediction)" if i==0 else ""))
    
    
