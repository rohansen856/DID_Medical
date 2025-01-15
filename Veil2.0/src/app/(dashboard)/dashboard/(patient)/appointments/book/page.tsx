"use client"

import { useState } from "react"
import { format } from "date-fns"
import { SearchIcon } from "lucide-react"
import { Label } from "recharts"

import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"

// Sample doctor data (replace with actual Prisma data fetching)
const sampleDoctors = [
  {
    id: 1,
    name: "Dr. Sarah Johnson",
    specialty: "Cardiologist",
    joinDate: "2021-05-15",
    prescriptionsIssued: 150,
  },
  {
    id: 2,
    name: "Dr. Mark Lee",
    specialty: "Dermatologist",
    joinDate: "2020-08-10",
    prescriptionsIssued: 85,
  },
  {
    id: 3,
    name: "Dr. Emma Brown",
    specialty: "Pediatrician",
    joinDate: "2019-03-21",
    prescriptionsIssued: 120,
  },
  {
    id: 4,
    name: "Dr. Jane Doe",
    specialty: "Neurosurgeon",
    joinDate: "2020-03-23",
    prescriptionsIssued: 100,
  },
]

const fetchDoctors = async (text, setSearchQuery) => {
  try {
    const response = await fetch("http://127.0.0.1:5000/get_recommendation", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ problem: text }),
    })
    if (!response.ok) {
      throw new Error("Network response was not ok")
    }
    const data = await response.json()
    console.log(data)
    setSearchQuery(data?.doctors[0] ?? "Neurosurgeon")
  } catch (error) {
    console.error("Failed to fetch doctors:", error)
    return []
  }
}

export default function AppointmentBookingPage() {
  const [doctors, setDoctors] = useState(sampleDoctors)
  const [searchQuery, setSearchQuery] = useState("")
  const [symptom, setSymptom] = useState("")

  // Filter doctors based on search query (by name or specialty)
  const filteredDoctors = doctors?.filter(
    (doctor) =>
      doctor?.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      doctor?.specialty.toLowerCase().includes(searchQuery.toLowerCase())
  )

  return (
    <div className="container mx-auto space-y-8 p-4">
      <h1 className="text-2xl font-bold">Book an Appointment</h1>

      {/* Search Bar */}
      <div className="mb-6 flex items-center gap-6">
        <SearchIcon className="mr-2 text-gray-500" />
        <Input
          type="text"
          placeholder="Search by doctor name or specialty"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="w-full"
        />
        <Dialog>
          <DialogTrigger asChild>
            <Button>Ask AI ✨</Button>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>AI recommends ✨</DialogTitle>
            </DialogHeader>

            <div className="grid gap-4">
              <div className="grid gap-2">
                <Label>Email</Label>
                <Textarea
                  onChange={(e) => setSymptom(e.target.value)}
                  id="email"
                  placeholder="Enter your symptoms here"
                  required
                  rows={6}
                />
              </div>
              <DialogClose>
                <Button
                  type="submit"
                  className="w-full"
                  onClick={async () => {
                    const doctors = await fetchDoctors(symptom, setSearchQuery)
                  }}
                >
                  Ask AI ✨
                </Button>
              </DialogClose>

              <DialogClose>
                <Button variant="outline" className="w-full">
                  Cancel
                </Button>
              </DialogClose>
            </div>
          </DialogContent>
        </Dialog>
      </div>

      {/* Doctor List */}
      <section className="space-y-4">
        {filteredDoctors.length > 0 ? (
          filteredDoctors.map((doctor) => (
            <Card key={doctor.id} className="shadow-sm relative">
              <CardHeader>
                <CardTitle>{doctor.name}</CardTitle>
                <CardDescription>Specialty: {doctor.specialty}</CardDescription>
              </CardHeader>
              <CardContent>
                <p>
                  <strong>Join Date:</strong>{" "}
                  {format(new Date(doctor.joinDate), "MMMM dd, yyyy")}
                </p>
                <p>
                  <strong>Prescriptions Issued:</strong>{" "}
                  {doctor.prescriptionsIssued}
                </p>
                <Badge variant="outline" className="mt-2">
                  {doctor.specialty}
                </Badge>
                <Button className="absolute right-5 bottom-5" onClick={(e) => {e.currentTarget.innerText = "Pending";e.currentTarget.classList.add("bg-yellow-500")}}>
                  Book Appointment now
                </Button>
              </CardContent>
            </Card>
          ))
        ) : (
          <p>No doctors found for the specified search.</p>
        )}
      </section>
    </div>
  )
}
