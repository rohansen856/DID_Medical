"use client"

import { useEffect, useState } from "react"
import { format } from "date-fns"
import { SearchIcon } from "lucide-react"

import { Badge } from "@/components/ui/badge"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"

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
]

export default function AppointmentBookingPage() {
  const [doctors, setDoctors] = useState(sampleDoctors)
  const [searchQuery, setSearchQuery] = useState("")

  // Filter doctors based on search query (by name or specialty)
  const filteredDoctors = doctors.filter(
    (doctor) =>
      doctor.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      doctor.specialty.toLowerCase().includes(searchQuery.toLowerCase())
  )

  return (
    <div className="container mx-auto space-y-8 p-4">
      <h1 className="text-2xl font-bold">Book an Appointment</h1>

      {/* Search Bar */}
      <div className="mb-6 flex items-center">
        <SearchIcon className="mr-2 text-gray-500" />
        <Input
          type="text"
          placeholder="Search by doctor name or specialty"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="w-full"
        />
      </div>

      {/* Doctor List */}
      <section className="space-y-4">
        {filteredDoctors.length > 0 ? (
          filteredDoctors.map((doctor) => (
            <Card key={doctor.id} className="shadow-sm">
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
