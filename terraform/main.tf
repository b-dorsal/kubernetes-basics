

# Create the project
resource "google_project" "gke_project" {
    name            = var.project_id
    project_id      = var.project_id
}

resource "google_project_service" "project_services" {
    for_each                    = toset(var.enabled_services)
    project                     = google_project.gke_project.project_id
    service                     = each.value
    disable_on_destroy          = false
    disable_dependent_services  = false
}

