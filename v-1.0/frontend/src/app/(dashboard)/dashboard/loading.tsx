import { DashboardHeader } from "@/components/header"
import { Icons } from "@/components/icons"
import { AppointmentCreateButton } from "@/components/post-create-button"
import { PostItem } from "@/components/post-item"
import { DashboardShell } from "@/components/shell"

export default function DashboardLoading() {
  return (
    <DashboardShell className="relative h-[80vh]">
      <DashboardHeader
        heading="Loading..."
        text="Please wait a minute while we fetch the details"
      >
        <AppointmentCreateButton />
      </DashboardHeader>
      <div className="absolute left-1/2 top-1/2 flex w-full -translate-x-1/2 -translate-y-1/2">
        <Icons.logo className="m-auto size-40 animate-pulse" />
      </div>
    </DashboardShell>
  )
}
