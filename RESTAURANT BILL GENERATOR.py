print("======RESTAURANT BILL GENERATOR========")
print("PLEASE ENTER THE DETAILS BELOW TO GENERATE THE BILL")
name = input("ENTER THE NAME OF THE CUSTOMER : ")
time = input("ENTER THE TIME OF THE DINING/BUYING OF CUSTOMER : ")
food = input("ENTER THE FOOD ITEM TAKEN BY CUSTOMER :")
quantity = int(input("ENTER THE QUANTITY OF FOOD TAKEN BY CUSTOMER :"))
price = float(input("ENTER PRICE PER ITEM : "))
total_price = (quantity * price)
print(f"""=================================================
                                BILL
   =================================================================
          NAME OF CUSTOMER              :          {name}
          TIME OF BUYING/DINING         :          {time}
          FOOD ITEM                     :          {food}
          QUANTITY OF FOOD ITEM TAKEN   :          {quantity}
          
          TOTAL BILL                    :          ${total_price}(inclusive of all taxes)
          
                                    END OF BILL
          
  =========================================================================================================""")
  #END OF CODE        
          
                                
