
from NormalizeDatabase.models import RawData, Hospitals, HospitalExpenses


class GetExpense:
    def __init__(self, request_hospital_id):
        self.request_hospital_id = request_hospital_id

    def get_expense_details(self):
        context = {}

        if Hospitals.objects.filter(HospitalID=self.request_hospital_id):
            print("Hospital found")
            hospital = Hospitals.objects.get(HospitalID=self.request_hospital_id)
            if HospitalExpenses.objects.filter(HospitalID=hospital):
                print("expenses found")
                expenses = HospitalExpenses.objects.filter(HospitalID=hospital)
                for expense_record in expenses:
                    raw_data = RawData.objects.get(RecordNumber=expense_record.RecordNumber.RecordNumber)
                    context[raw_data.RecordNumber] = {"HospitalID": hospital.HospitalID,
                                                      "RecordNumber": raw_data.RecordNumber,
                                                      "HospitalName": hospital.HospitalName,
                                                      "CharityCost": expense_record.CharityCost,
                                                      "BadDebtExpense": expense_record.BadDebtExpense,
                                                      "UncompasatedCost": expense_record.UncompasatedCost,
                                                      "TotalCost": expense_record.TotalCost,
                                                      "WageRelatedCostsCore": expense_record.WageRelatedCostsCore,
                                                      "WageRelatedCostsRHC": expense_record.WageRelatedCostsRHC,
                                                      "SalariesPayable": expense_record.SalariesPayable,
                                                      "ContractLabor": expense_record.ContractLabor,
                                                      "WageRelatedCostsTeaching": expense_record.WageRelatedCostsTeaching,
                                                      "WageRelatedCostInternResidents": expense_record.WageRelatedCostInternResidents,
                                                      "DepreciationCost": expense_record.DepreciationCost,
                                                      "FiscalYearBegin": expense_record.FiscalYearBegin,
                                                      "FiscalYearEnd": expense_record.FiscalYearEnd
                                                      }
                return context
            return {"message": "Hospital expense not found"}
        return {"message": "hospital not found"}

