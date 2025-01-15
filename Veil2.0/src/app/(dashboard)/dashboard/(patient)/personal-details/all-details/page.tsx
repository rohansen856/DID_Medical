import { mongo } from "@/lib/mongo"
import {
  demoData,
  PatientHistoryData,
} from "@/components/patient-detail-schema"

async function insertPatientHistory(patientHistoryData: PatientHistoryData) {
  try {
    for (const key of Object.keys(patientHistoryData)) {
      const collection = mongo.collection(key)
      await collection.insertOne(patientHistoryData[key])
      console.log(`New patient history data created for collection: ${key}`)
    }
  } catch (error) {
    console.error("Error inserting patient history data:", error)
  }
}

export default async function page() {
  // await insertPatientHistory(demoData)
  const data: any[] = []
  try {
    for (const key of Object.keys(demoData)) {
      const collection = mongo.collection(key)
      const result = await collection.findOne({})
      data.push({ key, result })
    }
  } catch (error) {
    return <pre>{JSON.stringify(error)}</pre>
  }
  return (
    <div>
      <pre>
        <div className="m-4 bg-secondary p-8">
          {JSON.stringify(data, null, 2)}
        </div>
        <div className="h-12 w-full bg-red-600"></div>
      </pre>
    </div>
  )
}
