import { useState } from "react"
import { redirect } from "next/navigation"
import { Appointment } from "@prisma/client"
import { CalendarIcon, ClipboardIcon } from "lucide-react"

import { db } from "@/lib/db"
import { getCurrentUser } from "@/lib/session"
import { cn } from "@/lib/utils"
import { Badge } from "@/components/ui/badge"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { DashboardHeader } from "@/components/header"
import { AppointmentCreateButton } from "@/components/post-create-button"
import { DashboardShell } from "@/components/shell"

export default async function Appointments() {
  const user = await getCurrentUser()
  if (!user || !user.id) return redirect("/login")

  const appointments = await db.appointment.findMany({
    where: {
      patient: {
        userId: user.id,
      },
    },
    select: {
      startTime: true,
      endTime: true,
      id: true,
      doctorId: true,
      status: true,
      doctor: {
        select: {
          mbbsId: true,
          user: {
            select: {
              name: true,
            },
          },
        },
      },
    },
  })

  // Separate upcoming and past appointments based on the current date
  const upcomingAppointments = appointments.filter(
    (appointment) => new Date(appointment.startTime) >= new Date()
  )
  const pastAppointments = appointments.filter(
    (appointment) => new Date(appointment.startTime) < new Date()
  )

  return (
    <DashboardShell>
      <DashboardHeader
        heading="Appointments"
        text="Create and manage your appointments."
      >
        <AppointmentCreateButton />
      </DashboardHeader>
      <div className="container mx-auto space-y-8 p-4">
        <h1 className="text-2xl font-bold">Appointments</h1>

        {/* Upcoming Appointments Section */}
        <section>
          <h2 className="mb-4 text-xl font-semibold">Upcoming Appointments</h2>
          <div className="space-y-4">
            {upcomingAppointments.length > 0 ? (
              upcomingAppointments.map((appointment) => (
                <Card
                  key={appointment.id}
                  className="flex items-center justify-between shadow-sm"
                >
                  <CardHeader>
                    <CardTitle className="text-lg">
                      {appointment.doctor.user.name} (
                      {appointment.doctor.mbbsId})
                    </CardTitle>
                    <CardDescription>
                      <CalendarIcon className="mr-2 inline" />
                      {appointment.startTime.toLocaleString()} -{" "}
                      {appointment.endTime.toLocaleString()}
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    {/* <p>
                      <strong>Reason:</strong> {appointment.}
                    </p>
                    <p>
                      <strong>Notes:</strong> {appointment.notes}
                    </p> */}
                    <Badge
                      className={cn(
                        "mt-2",
                        appointment.status === "PENDING" && "bg-yellow-600",
                        appointment.status === "CONFIRMED" && "bg-green-600",
                        appointment.status === "CANCELED" && "bg-red-600"
                      )}
                      variant="outline"
                    >
                      {appointment.status}
                    </Badge>
                  </CardContent>
                </Card>
              ))
            ) : (
              <p>No upcoming appointments.</p>
            )}
          </div>
        </section>

        {/* Past Appointments Section */}
        <section>
          <h2 className="mb-4 text-xl font-semibold">Past Appointments</h2>
          <div className="space-y-4">
            {pastAppointments.length > 0 ? (
              pastAppointments.map((appointment) => (
                <Card
                  key={appointment.id}
                  className="flex items-center justify-between shadow-sm"
                >
                  <CardHeader>
                    <CardTitle className="text-lg">
                      {appointment.doctor.user.name} (
                      {appointment.doctor.mbbsId})
                    </CardTitle>
                    <CardDescription>
                      <CalendarIcon className="mr-2 inline" />
                      {appointment.startTime.toLocaleString()} at{" "}
                      {appointment.endTime.toLocaleString()}
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    {/* <p>
                      <strong>Reason:</strong> {appointment.reason}
                    </p>
                    <p>
                      <strong>Notes:</strong> {appointment.notes}
                    </p> */}
                    <Badge
                      className={cn(
                        "mt-2",
                        appointment.status === "PENDING" && "bg-yellow-600",
                        appointment.status === "CONFIRMED" && "bg-green-600",
                        appointment.status === "CANCELED" && "bg-red-600"
                      )}
                      variant="outline"
                    >
                      {appointment.status}
                    </Badge>
                  </CardContent>
                </Card>
              ))
            ) : (
              <p>No past appointments.</p>
            )}
          </div>
        </section>
      </div>
    </DashboardShell>
  )
}
